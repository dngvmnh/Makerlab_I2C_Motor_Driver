# Makerlab I2C Motor Driver Library Documentation

## Overview
The `I2C_Motor_Driver` library is designed to control DC motors using the I2C communication protocol. This library allows users to interface with a motor driver through an I2C bus, setting motor speed and direction.

## Initialization
```python
from I2C_Motor_Driver import Makerlabvn_I2C_Motor_Driver
from machine import I2C, Pin

i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Initialize I2C
motor_driver = Makerlabvn_I2C_Motor_Driver(i2c, 0x40)  # Initialize Motor Driver with address 0x40
motor_driver.begin()  # Prepare the motor driver
```

## Class: `Makerlabvn_I2C_Motor_Driver`

### Attributes
- `MAKERLABVN_I2C_DRIVER_SLAVE_ADDRESS_MIN`: Minimum I2C address (0x10)
- `MAKERLABVN_I2C_DRIVER_SLAVE_ADDRESS_MAX`: Maximum I2C address (0x7F)
- `DELAY_I2C_SEND`: Delay after sending I2C data (20ms)

### Methods
#### `begin()`
Initializes the motor driver by stopping all DC and RC motors.

#### `MA(direction, speed)`
Controls motor A.
- `direction`: 1 for forward, 0 for backward
- `speed`: 0 to 255

#### `MB(direction, speed)`
Controls motor B.
- `direction`: 1 for forward, 0 for backward
- `speed`: 0 to 255

#### `writeMA(direction, speed_percentagecentSpeed)`
Sets motor A speed in speed_percentagecentage (0-100%).

#### `writeMB(direction, speed_percentagecentSpeed)`
Sets motor B speed in speed_percentagecentage (0-100%).

#### `freeS1()`
Stops servo motor S1.

#### `freeS2()`
Stops servo motor S2.

## Example Usage (main.py)
```python
from I2C_Motor_Driver import Makerlabvn_I2C_Motor_Driver
from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21))  
motor_driver = Makerlabvn_I2C_Motor_Driver(i2c, 0x40)
motor_driver.begin()

def forward(second, speed_percentage):
    motor_driver.writeMA(1, speed_percentage)
    motor_driver.writeMB(1, speed_percentage)
    time.sleep(second)
    stop(0.5)

def stop(second):
    motor_driver.writeMA(0, 0)
    motor_driver.writeMB(0, 0)
    time.sleep(second)

forward(1, 100)  # Move forward for 1 secondond at full speed
```

