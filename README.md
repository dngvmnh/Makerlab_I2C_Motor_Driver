# Makerlab I2C Motor Driver Library Documentation (Mecanum Wheels)

## Overview
The `I2C_Motor_Driver` library is designed to control **Mecanum wheel** robots using the **I2C communication protocol**. This library enables control over **4 independent motors** for omnidirectional movement.

## Initialization
```python
from I2C_Motor_Driver import Makerlabvn_I2C_Motor_Driver
from machine import I2C, Pin

i2c = I2C(1, scl=Pin(22), sda=Pin(21))  # Initialize I2C bus
motor_driver_0 = Makerlabvn_I2C_Motor_Driver(i2c, 0x41)  # Motor driver 1 (Front motors)
motor_driver_1 = Makerlabvn_I2C_Motor_Driver(i2c, 0x40)  # Motor driver 2 (Rear motors)

motor_driver_0.begin()
motor_driver_1.begin()
```

## Class: `Makerlabvn_I2C_Motor_Driver`
### Attributes
- `MAKERLABVN_I2C_DRIVER_SLAVE_ADDRESS_MIN`: Minimum I2C address (0x10)
- `MAKERLABVN_I2C_DRIVER_SLAVE_ADDRESS_MAX`: Maximum I2C address (0x7F)
- `DELAY_I2C_SEND`: Delay after sending I2C data (20ms)

### Methods
#### `begin()`
Initializes the motor driver by stopping all motors.

#### `MA(direction, speed)`, `MB(direction, speed)`, `MC(direction, speed)`, `MD(direction, speed)`
Controls motors individually.
- `direction`: 1 for forward, 0 for backward
- `speed`: 0 to 255

#### `writeMA(direction, speed_percentage)`, `writeMB(direction, speed_percentage)`, `writeMC(direction, speed_percentage)`, `writeMD(direction, speed_percentage)`
Sets motor speed in percentage (0-100%).

#### `freeS1()`, `freeS2()`
Stops servo motors.

## Mecanum Wheel Movements

### **Forward**
```python
def forward(sec, speed):
    motor_driver_0.writeMA(1, speed)  # Front-left
    motor_driver_0.writeMB(1, speed)  # Front-right
    motor_driver_1.writeMC(1, speed)  # Rear-left
    motor_driver_1.writeMD(1, speed)  # Rear-right
    time.sleep(sec)
    stop(0.5)
```

### **Backward**
```python
def backward(sec, speed):
    motor_driver_0.writeMA(0, speed)
    motor_driver_0.writeMB(0, speed)
    motor_driver_1.writeMC(0, speed)
    motor_driver_1.writeMD(0, speed)
    time.sleep(sec)
    stop(0.5)
```

### **Strafe Left**
```python
def strafe_left(sec, speed):
    motor_driver_0.writeMA(0, speed)
    motor_driver_0.writeMB(1, speed)
    motor_driver_1.writeMC(1, speed)
    motor_driver_1.writeMD(0, speed)
    time.sleep(sec)
    stop(0.5)
```

### **Strafe Right**
```python
def strafe_right(sec, speed):
    motor_driver_0.writeMA(1, speed)
    motor_driver_0.writeMB(0, speed)
    motor_driver_1.writeMC(0, speed)
    motor_driver_1.writeMD(1, speed)
    time.sleep(sec)
    stop(0.5)
```

### **Rotate Left (Counterclockwise)**
```python
def rotate_left(sec, speed):
    motor_driver_0.writeMA(0, speed)
    motor_driver_0.writeMB(1, speed)
    motor_driver_1.writeMC(0, speed)
    motor_driver_1.writeMD(1, speed)
    time.sleep(sec)
    stop(0.5)
```

### **Rotate Right (Clockwise)**
```python
def rotate_right(sec, speed):
    motor_driver_0.writeMA(1, speed)
    motor_driver_0.writeMB(0, speed)
    motor_driver_1.writeMC(1, speed)
    motor_driver_1.writeMD(0, speed)
    time.sleep(sec)
    stop(0.5)
```

### **Stop**
```python
def stop(sec):
    motor_driver_0.writeMA(0, 0)
    motor_driver_0.writeMB(0, 0)
    motor_driver_1.writeMC(0, 0)
    motor_driver_1.writeMD(0, 0)
    time.sleep(sec)
```

## Example Usage (main.py)
```python
import time

strafe_right(2, 80)  # Strafe right for 2 seconds at 80% speed
rotate_left(1, 100)  # Rotate counterclockwise for 1 second at full speed
forward(3, 100)  # Move forward for 3 seconds at full speed
stop(1)  # Stop for 1 second
```

---

### 🎯 **Features:**
✔ Supports **4-motor Mecanum wheel robots**  
✔ Allows **omnidirectional movement**  
✔ Uses **I2C communication** for efficient control  
