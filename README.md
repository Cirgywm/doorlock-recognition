# Automatic Door Lock Security System with Face Recognition Using MobileNetV3 Small and Arduino UNO
![image](https://github.com/user-attachments/assets/f40eee1b-2c57-459f-9c08-33717252f2ba)

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
