from I2C_Motor_Driver import Makerlabvn_I2C_Motor_Driver
from machine import I2C, Pin
import time


i2c = I2C(0, scl=Pin(22), sda=Pin(21))  
devices = i2c.scan()
trans=0.5

motor_driver = Makerlabvn_I2C_Motor_Driver(i2c, 0x40)
motor_driver.begin()

def forward(sec, per):
    motor_driver.writeMA(1, per)
    motor_driver.writeMB(1, per)
    time.sleep(sec)
    stop(trans)
    
def backward(sec, per):
    motor_driver.writeMA(0, per)
    motor_driver.writeMB(0, per)
    time.sleep(sec)
    stop(trans)
    
def turnL(sec, per):
    motor_driver.writeMA(0,per)
    motor_driver.writeMB(1,per)
    time.sleep(sec)
    stop(trans)
    
def turnR(sec, per):
    motor_driver.writeMA(1,per)
    motor_driver.writeMB(0,per)
    time.sleep(sec)
    stop(trans)
    
def stop(sec):
    motor_driver.writeMA(0, 0)
    motor_driver.writeMB(0, 0)
    time.sleep(sec)

    
forward(1, 100)
turnR(1, 100)
backward(1, 100)
turnL(1, 100)

    
    

