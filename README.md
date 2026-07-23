# Automatic Door Lock Security System with Face Recognition Using MobileNetV3 Small and Arduino UNO
![WhatsApp Image 2024-12-07 at 19 18 07_944e0310](https://github.com/user-attachments/assets/de7167b2-3a39-469e-84ac-ed8e91d08938)

## Project Domain
This project is an access control system using facial recognition with an Arduino UNO and a MobileNetV3 Small based model architecture.

### Problem Statements
- Traditional door locking systems based on physical keys or access cards carry the risk of being lost or stolen.
- Manual unlocking reduces time efficiency, especially in busy environments.
- Many smart door locking systems rely on internet and cloud connections, which increases their latency, dependency on the network, and their vulnerability to tampering or cyberattacks.

### Goals
- Using a MobileNetV3 Small-based system to authenticate authorized personnel, increases security and reduces human error.
- Increase efficiency by enabling touchless operations and fast authentication processes.
- Facial recognition models are implemented directly on edge devices to reduce latency and dependency on internet networks. 

### Solution Statements
- Integrate a camera or webcam for capturing facial images for recognition.
- PC side to process the vision model.
- Microcontroller side (Arduino UNO) to control the system and process the results of facial recognition.
- Include a solenoid door lock to grant or deny physical access based on recognition results.
- Employ a confidence-based rejection system to mark unrecognized faces and deny access.


## Edge System Planning
### Edge System Diagram
![edge system](https://github.com/Ach111es/doorlock-recognition/blob/f8b011c886d6996db2c93a42fb08dda7257aa94b/assets/edge_diagram.png)

### System State Diagram
- **Edge Gateway**

![edge gateway state diagram](https://github.com/Ach111es/doorlock-recognition/blob/f8b011c886d6996db2c93a42fb08dda7257aa94b/assets/state_diagram_gateway.png)

- **Edge Device**

![edge device state diagram](https://github.com/Ach111es/doorlock-recognition/blob/f8b011c886d6996db2c93a42fb08dda7257aa94b/assets/state_diagram_doorlock.png)


## Prerequisites
### Component Preparation

- **Arduino UNO**: Microcontroller for processing facial recognition results and controlling the system.
- **5V Relay Module**: Switches the solenoid door lock based on recognition results.
- **Solenoid Door Lock**: Secures the door, unlocking only for authorized individuals.
- **Camera**: Captures facial images for recognition.
- **Buzzer**: Provides audio alerts for access status (granted/denied).
- **12V Power Supply**: External power for solenoid door lock.

### Datasheet Arduino Uno R3
![arduino uno r3 datasheet](https://github.com/Ach111es/doorlock-recognition/blob/f8b011c886d6996db2c93a42fb08dda7257aa94b/assets/ArduinoUNOrev3.png)

### System Schematic
![system schematic](https://github.com/Ach111es/doorlock-recognition/blob/f8b011c886d6996db2c93a42fb08dda7257aa94b/assets/Schematic_HomeSecurity.png)


## Demo and Evaluation
- **Setup**: Connect all components as per the wiring diagram and run the final code blok on the .ipynb file.
- **Demo**: Demonstrate real-time face recognition of authorized and people, along with automatic solenoid door lock opening.
- **Evaluation**: Test the system with different faces and evaluate the prediction scores.

### Real-time Face Recognition
| ![WhatsApp Image 2024-12-07 at 17 30 25_ff744b9f](https://github.com/user-attachments/assets/bce25ab8-44f5-4fd3-bb79-4ca32cd8554e) | ![WhatsApp Image 2024-12-07 at 17 32 27_385936e0](https://github.com/user-attachments/assets/00f9f7ce-a95c-4714-b6ab-0e4b099be4cd) |
| ----------- | ----------- |
| ![WhatsApp Image 2024-12-07 at 17 33 28_7b4f9bf3](https://github.com/user-attachments/assets/c8670246-6cf9-4315-b159-68ae1481f058) | ![WhatsApp Image 2024-12-07 at 17 34 00_882837fd](https://github.com/user-attachments/assets/c20ebeb5-ec6c-4192-a899-559a1b1aadc7) |

### Door Lock System

*Click the embedded youtube video below to watch

[![Demo Video](https://img.youtube.com/vi/VgoxX6TS_PM/0.jpg)](https://www.youtube.com/watch?v=VgoxX6TS_PM)
