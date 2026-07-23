import pyfirmata as fir
import time
import torch
import torchvision.transforms as transforms
import cv2
from model import MultiClassClassificationModel


port = 'COM4' #Change depending on available port
HIGH = True
LOW = False

# ====== Communication initialization
try:
    board = fir.Arduino(port)
    print("Connected to the board successfully.")
    time.sleep(2)
except Exception as e:
    print(f"Error connecting to the board: {e}")


# ====== Pin initialization
# Actuators
buzzer = board.get_pin('d:11:p')  # D11 - output PWM
solenoid = board.get_pin('d:12:o')  # D12 - output digital


# ====== Load Model
model = MultiClassClassificationModel(num_classes=4)  # Replace 4 with the number of your classes
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.load_state_dict(torch.load("best_model.pth", map_location=torch.device('cpu')))
model.to(device)
model.eval()

class_names = ['Abraar', 'Aldy', 'Dimas', 'Haikal'] # Change depending on your class labels
authorized = ['Dimas', 'Haikal'] 

# Image resize and normalization
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((160, 160)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])
])


# ====== Function
def door_open():
    global buzzer, solenoid
    buzzer.write(HIGH)
    buzzer.write(LOW)
    solenoid.write(HIGH)


def door_close():
    global buzzer, solenoid
    for i in range(2):
        solenoid.write(LOW)
        buzzer.write(HIGH)
        buzzer.write(LOW)


def test_func():
    while True:
        user_input = int(input("Input: "))
        if user_input == 1:
            try:
                print("Write successful")
            except Exception as e:
                print(f"Error writing to solenoid: {e}")
            print("contacting")
            solenoid.write(HIGH)
            time.sleep(5)
            print("contacted")
            solenoid.write(LOW)
        elif user_input == 2:
            # led_builtin.write(LOW)
            buzzer.write(HIGH)
            time.sleep(1)
            buzzer.write(LOW)
        elif user_input == 3:
            door_open()
        elif user_input == 4:
            door_close()
        elif user_input == 0:
            break


# Function to predict a single frame
def predict_frame(frame):
    img_tensor = transform(frame).unsqueeze(0)
    with torch.no_grad():
        outputs = model(img_tensor)
        probabilities = F.softmax(outputs, dim=1)
        max_prob, predicted = torch.max(probabilities, 1)
    return class_names[predicted.item()], max_prob.item()


# ====== Main Logic
auth_label = "Authorized"
#prediction_buffer = deque(maxlen=30)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Convert frame to RGB for prediction (OpenCV uses BGR by default)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    predicted_label, score = predict_frame(frame_rgb)

    # Display the prediction and score on the frame
    cv2.putText(frame, f'Prediction: {predicted_label} ({score:.2f})', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    if predicted_label in authorized :
        door_open()
        #time.sleep(5)
        door_close()
        cv2.putText(frame, auth_label, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        print("Face not recognized")
        cv2.putText(frame, 'Unauthorized', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
    # Show the frame
    cv2.imshow('Real-Time Prediction', frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# ======  Release resources
cap.release()
cv2.destroyAllWindows()


# ====== Closing communication with arduino
board.exit()

