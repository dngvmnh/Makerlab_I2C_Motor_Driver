import utime
import sys
import select
from machine import I2C, Pin
from Makerlab_I2C_Motor_Driver import Makerlabvn_I2C_Motor_Driver

i2c = I2C(1, scl=Pin(22), sda=Pin(21))
motor_driver_0 = Makerlabvn_I2C_Motor_Driver(i2c, 0x41)
motor_driver_1 = Makerlabvn_I2C_Motor_Driver(i2c, 0x40)
motor_driver_0.begin()
motor_driver_1.begin()

per = 50  
running = True  

def key_pressed():
    return select.select([sys.stdin], [], [], 0)[0]

def forward():
    print("Moving forward")
    motor_driver_0.writeMA(1, per)
    motor_driver_0.writeMB(1, per)
    motor_driver_1.writeMC(1, per)
    motor_driver_1.writeMD(1, per)

def backward():
    print("Moving backward")
    motor_driver_0.writeMA(0, per)
    motor_driver_0.writeMB(0, per)
    motor_driver_1.writeMC(0, per)
    motor_driver_1.writeMD(0, per)

def turn_left():
    print("Turning left")
    motor_driver_0.writeMA(0, per)
    motor_driver_0.writeMB(1, per)
    motor_driver_1.writeMC(0, per)
    motor_driver_1.writeMD(1, per)

def turn_right():
    print("Turning right")
    motor_driver_0.writeMA(1, per)
    motor_driver_0.writeMB(0, per)
    motor_driver_1.writeMC(1, per)
    motor_driver_1.writeMD(0, per)

def stop():
    print("Stopping")
    motor_driver_0.writeMA(0, 0)
    motor_driver_0.writeMB(0, 0)
    motor_driver_1.writeMC(0, 0)
    motor_driver_1.writeMD(0, 0)

print("Use W/A/S/D to move, X to stop, and Q to quit.")
while running:
    if key_pressed():
        key = sys.stdin.read(1).lower()  

        if key == 'w':
            forward()
        elif key == 's':
            backward()
        elif key == 'a':
            turn_left()
        elif key == 'd':
            turn_right()
        elif key == 'x':
            stop()
        elif key == 'q':
            stop()
            print("Control exited")
            running = False

    utime.sleep(0.1)  
