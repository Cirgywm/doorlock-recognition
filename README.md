# Automatic Door Lock Security System with Face Recognition Using MobileNetV3 Small and Arduino UNO

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
- Use an Arduino UNO to control the system and process facial recognition.
- Include a solenoid door lock to grant or deny physical access based on recognition results.
- Employ a confidence-based rejection system to mark unrecognized faces and deny access.

## Prerequisites
### Component Preparation

- **Arduino UNO**: Microcontroller for processing facial recognition results and controlling the system.
- **5V Relay Module**: Switches the solenoid door lock based on recognition results.
- **Solenoid Door Lock**: Secures the door, unlocking only for authorized individuals.
- **Camera**: Captures facial images for recognition.
- **Buzzer**: Provides audio alerts for access status (granted/denied).
- **12V Power Supply**: Powers the solenoid door lock and other components.

### System Schematic
![WhatsApp Image 2024-12-02 at 12 40 34_531ea401](https://github.com/user-attachments/assets/1bf02ffb-beda-4627-8bf4-b76df8da306c)

### System State Diagram
- **Edge Gateway**

![image](https://github.com/user-attachments/assets/b05f42f8-f6e7-4f43-9655-ecdf67832d53)

- **Edge Device**

![image](https://github.com/user-attachments/assets/be3ec3f7-22bb-42bf-8d1f-de9076a42344)
