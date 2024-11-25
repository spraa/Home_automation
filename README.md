# Home_automation
# Home Automation Using Arduino Uno and Python (Bluetooth Controlled)

A simple home automation project that demonstrates controlling devices using **Arduino Uno**, **HC-05 Bluetooth module**, and **Python**. The project allows you to control up to 4 devices (or LEDs) wirelessly via a Python program.

---

## 🚀 Features
- Control 4 devices using Bluetooth commands.
- Use Python to send ON/OFF commands to the Arduino.
- Easy-to-build circuit using basic components.

---

## 🛠️ Components Required
- **Arduino Uno**
- **HC-05 Bluetooth Module**
- **4 LEDs** (or appliances controlled via relays)
- **Resistors** (220 ohms for LEDs)
- **Breadboard & Jumper Wires**

---

## ⚡ Circuit Diagram
![Circuit Diagram](Images/circuit_diagram.jpg)

---

## 💻 How It Works
1. **Connect the Circuit**:  
   - Connect the HC-05 Bluetooth module to Arduino (TX, RX, VCC, GND).
   - Connect LEDs (or relays) to Arduino pins **2, 3, 4, and 5**.

2. **Upload Arduino Code**:  
   Upload the provided `HomeAutomation.ino` code to your Arduino Uno.

3. **Run Python Script**:  
   Use the `home_automation.py` script to send Bluetooth commands to control the devices.

4. **Control Devices**:  
   - Use commands `1`, `2`, `3`, `4` to turn ON devices.
   - Use commands `5`, `6`, `7`, `8` to turn OFF devices.

---

## 🧩 Arduino Code
You can find the Arduino code [here](Home_automation/Arduino/HomeAutomation.ino.txt).

---

## 🐍 Python Code
You can find the Python script [here](Python/home_automation.py).

---

## 🖼️ Demo
Photo showcasing the project in action.  
Example:  
![Project Demo](Images/project_demo.jpg)

---

## 📂 Folder Structure
```plaintext
HomeAutomation-Bluetooth-Arduino
│
├── Arduino
│   ├── HomeAutomation.ino      # Arduino code
│
├── Python
│   ├── home_automation.py      # Python script
│
├── Images
│   ├── circuit_diagram.jpg     # Circuit diagram image
│   ├── project_demo.jpg        # Demo image of your project
│
├── README.md                   # Documentation for the project


