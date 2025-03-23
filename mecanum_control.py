from Makerlab_I2C_Motor_Driver import Makerlabvn_I2C_Motor_Driver
from machine import I2C, Pin
import time, utime

i2c = I2C(1, scl=Pin(22), sda=Pin(21))  
devices = i2c.scan()
trans=0.5
t=1
per=50

motor_driver_0 = Makerlabvn_I2C_Motor_Driver(i2c, 0x40)
motor_driver_1 = Makerlabvn_I2C_Motor_Driver(i2c, 0x41)
motor_driver_0.begin()
motor_driver_1.begin()

def check_motor_drivers():
    if devices:
        print("I2C Drivers:")
        for device in devices:
            print(" - Address: 0x{:02X}".format(device))
    else:
        print("No I2C drivers found.")
        
    motor_drivers = []
    for address in devices:
        try:
            driver = Makerlabvn_I2C_Motor_Driver(i2c, address)
            driver.begin()
            motor_drivers.append(driver)
            print(f"Initialized Motor Driver at address 0x{address:02X}")
        except Exception as e:
            print(f"Failed to initialize Motor Driver at address 0x{address:02X}: {e}")

def t_forward(sec, per):
    print("forwarding")
    
    start_time = utime.ticks_ms()

    motor_driver_0.writeMA(1, per)
    motor_driver_0.writeMB(1, per)
    motor_driver_1.writeMC(1, per)
    motor_driver_1.writeMD(1, per)

    while utime.ticks_ms() - start_time < sec * 1000:
        pass 

    stopM0()
    stopM1()
    
def t_backward(sec, per):
    print("backwarding")
    
    start_time = utime.ticks_ms()

    motor_driver_0.writeMA(0, per)
    motor_driver_0.writeMB(0, per)
    motor_driver_1.writeMC(0, per)
    motor_driver_1.writeMD(0, per)

    while utime.ticks_ms() - start_time < sec * 1000:
        pass 

    stopM0()
    stopM1()
    
def t_moveL(sec, per):
    print("moving left")
    
    start_time = utime.ticks_ms()

    motor_driver_0.writeMA(0, per)
    motor_driver_0.writeMB(1, per)
    motor_driver_1.writeMC(1, per)
    motor_driver_1.writeMD(0, per)

    while utime.ticks_ms() - start_time < sec * 1000:
        pass 

    stopM0()
    stopM1()    
    
def t_moveR(sec, per):
    print("moving right")
    
    start_time = utime.ticks_ms()

    motor_driver_0.writeMA(1, per)
    motor_driver_0.writeMB(0, per)
    motor_driver_1.writeMC(0, per)
    motor_driver_1.writeMD(1, per)

    while utime.ticks_ms() - start_time < sec * 1000:
        pass 

    stopM0()
    stopM1()
    
def t_diagonalL(sec, per):
    print("diagonaling left")
    
    start_time = utime.ticks_ms()

    motor_driver_0.writeMB(1, per)
    motor_driver_1.writeMC(1, per)

    while utime.ticks_ms() - start_time < sec * 1000:
        pass 

    stopM0()
    stopM1()
    
def t_diagonalR(sec, per):
    print("diagonaling right")
    
    start_time = utime.ticks_ms()

    motor_driver_0.writeMA(1, per)
    motor_driver_1.writeMD(1, per)

    while utime.ticks_ms() - start_time < sec * 1000:
        pass 

    stopM0()
    stopM1()
    
def t_concernL(sec, per):
    print("concerning left")
    
    start_time = utime.ticks_ms()

    motor_driver_0.writeMA(1, per)
    motor_driver_1.writeMC(1, per)

    while utime.ticks_ms() - start_time < sec * 1000:
        pass 

    stopM0()
    stopM1()
    
def t_concernR(sec, per):
    print("concerning right")
    
    start_time = utime.ticks_ms()

    motor_driver_0.writeMB(1, per)
    motor_driver_1.writeMD(1, per)

    while utime.ticks_ms() - start_time < sec * 1000:
        pass 

    stopM0()
    stopM1()
    
def t_turnL(sec, per):
    print("turing left")
    
    start_time = utime.ticks_ms()

    motor_driver_0.writeMA(0, per)
    motor_driver_0.writeMB(1, per)
    motor_driver_1.writeMC(0, per)
    motor_driver_1.writeMD(1, per)

    while utime.ticks_ms() - start_time < sec * 1000:
        pass 

    stopM0()
    stopM1()
    
def t_turnR(sec, per):
    print("turing right")
    
    start_time = utime.ticks_ms()

    motor_driver_0.writeMA(1, per)
    motor_driver_0.writeMB(0, per)
    motor_driver_1.writeMC(1, per)
    motor_driver_1.writeMD(0, per)

    while utime.ticks_ms() - start_time < sec * 1000:
        pass 

    stopM0()
    stopM1()
    
def t_rearL(sec, per):
    print("rearing left")
    
    start_time = utime.ticks_ms()

    motor_driver_1.writeMC(1, per)
    motor_driver_1.writeMD(0, per)

    while utime.ticks_ms() - start_time < sec * 1000:
        pass 

    stopM0()
    stopM1()
    
def t_rearR(sec, per):
    print("rearing right")
    
    start_time = utime.ticks_ms()

    motor_driver_1.writeMC(0, per)
    motor_driver_1.writeMD(1, per)

    while utime.ticks_ms() - start_time < sec * 1000:
        pass 

    stopM0()
    stopM1()
    
def stopM0():
    motor_driver_0.writeMA(0, 0)
    motor_driver_0.writeMB(0, 0)

def stopM1():
    motor_driver_1.writeMC(0, 0)
    motor_driver_1.writeMD(0, 0)

# check_motor_drivers()
time.sleep(5)
t_forward(t, per)
t_backward(t, per)
t_moveR(t, per)
t_moveL(t, per)
t_diagonalL(t, per)
t_diagonalR(t, per)
t_concernL(t, per)
t_concernR(t, per)
t_turnL(t, per)
t_turnR(t, per)
t_rearL(t, per)
t_rearR(t, per)



