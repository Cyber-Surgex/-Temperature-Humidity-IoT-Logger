# Temperature & Humidity IoT Logger — Arduino + Python

This project is a real-time **Temperature & Humidity Logger** using an Arduino and a DHT11 sensor.  
It reads sensor data via the Arduino, sends it to a computer using serial communication, and displays a **live dashboard** using Python and Matplotlib. The data is also logged into a CSV file for further analysis.

---

##  Features

- Real-time sensor data collection (temperature & humidity)
- Serial communication between Arduino and Python
- Live updating dashboard using Matplotlib
- Automatic CSV logging of sensor data
- Lightweight and beginner-friendly

---

##  Hardware Required

- Arduino Uno / Nano / Compatible Board  
- DHT11 Temperature & Humidity Sensor  
- Jumper Wires  
- (Optional) Breadboard  
- USB Cable to connect Arduino to PC

---

##  Wiring Instructions (Written Format)

Connect the DHT11 sensor to the Arduino as follows:

- **DHT11 VCC** → Connect to **Arduino 5V**  
- **DHT11 GND** → Connect to **Arduino GND**  
- **DHT11 DATA** → Connect to **Arduino Digital Pin 2**

>  **If using a raw DHT11 sensor (not on a module)**, add a **10kΩ resistor** between **DATA** and **VCC** to ensure stable readings.

---

##  Software Setup

### 1. **Arduino**
- Open `DHT11_Logger.ino` in the Arduino IDE
- Install the required libraries:
  - `DHT sensor library` by Adafruit
  - `Adafruit Unified Sensor`
- Upload the code to your Arduino board

### 2. **Python**
Install required packages:

```bash
pip install pyserial matplotlib
