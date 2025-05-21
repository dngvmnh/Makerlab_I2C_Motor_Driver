import network
import urequests
import time, utime
from Makerlab_I2C_Motor_Driver_Lib import Makerlabvn_I2C_Motor_Driver
from machine import I2C, Pin

SSID = "Dngvmnh"
PASSWORD = "Persistent2025"
ut = 0.001

SERVER_URL = "http://192.168.198.146:5000/command"

i2c = I2C(1, scl=Pin(8), sda=Pin(9))
motor_driver_0 = Makerlabvn_I2C_Motor_Driver(i2c, 0x40)
motor_driver_1 = Makerlabvn_I2C_Motor_Driver(i2c, 0x41)

print("Initializing motor drivers...")
motor_driver_0.begin()
motor_driver_1.begin()

SPEED = 85 

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(0.5)
    print("Connected to WiFi:", wlan.ifconfig())

def t_forward(per):
    stop()
    utime.sleep(ut)
    print("forwarding")
    motor_driver_0.writeMA(1, per)
    motor_driver_0.writeMB(1, per)
    motor_driver_1.writeMC(1, per)
    motor_driver_1.writeMD(1, per)
    
def t_backward(per):
    stop()
    utime.sleep(ut)
    print("backwarding")
    
    motor_driver_0.writeMA(0, per)
    motor_driver_0.writeMB(0, per)
    motor_driver_1.writeMC(0, per)
    motor_driver_1.writeMD(0, per)

    
def t_moveL(per):
    stop()
    utime.sleep(ut)
    print("moving left")
    
    motor_driver_0.writeMA(0, per)
    motor_driver_0.writeMB(1, per)
    motor_driver_1.writeMC(1, per)
    motor_driver_1.writeMD(0, per)
    
    
def t_moveR(per):
    stop()
    utime.sleep(ut)
    print("moving right")

    motor_driver_0.writeMA(1, per)
    motor_driver_0.writeMB(0, per)
    motor_driver_1.writeMC(0, per)
    motor_driver_1.writeMD(1, per)
    
def stop():
    print("Stopped")
    motor_driver_0.writeMA(0, 0)
    motor_driver_0.writeMB(0, 0)
    motor_driver_1.writeMC(0, 0)
    motor_driver_1.writeMD(0, 0)
    
def diagonal_right(per):
    stop()
    utime.sleep(ut)
    print("Diagonaling Right")
    motor_driver_0.writeMA(1, per)
    motor_driver_1.writeMD(1, per)
    
def diagonal_left(per):
    stop()
    utime.sleep(ut)
    print("Diagonaling Left")
    motor_driver_0.writeMB(1, per)
    motor_driver_1.writeMC(1, per)
    
def concern_left(per):
    stop()
    utime.sleep(ut)
    print("Concerning Left")
    motor_driver_0.writeMA(0, per)
    motor_driver_1.writeMD(0, per)
    
def concern_right(per):
    stop()
    utime.sleep(ut)
    print("Concerning Right")
    motor_driver_0.writeMB(0, per)
    motor_driver_1.writeMC(0, per)

def execute_action(action):
    stop()

    if action == "forward":
        t_forward(SPEED)

    elif action == "backward":
        t_backward(SPEED)

    elif action == "left":
        t_moveL(SPEED)

    elif action == "right":
        t_moveR(SPEED)
        
    elif action == "diagonal-left":
        diagonal_left(SPEED)
        
    elif action == "diagonal-right":
        diagonal_right(SPEED)
        
    elif action == "concern-right":
        concern_right(SPEED)
        
    elif action == "concern-left":
        concern_left(SPEED)

    elif action == "stop":
        stop()

def poll_server():
    last_action = None
    while True:
        try:
            res = urequests.get(SERVER_URL)
            data = res.json()
            res.close()
            print("Received data:", data)

            action = data.get("action", "stop")
            if action != last_action:
                execute_action(action)
                last_action = action
        except Exception as e:
            print("Error fetching command:", e)

        time.sleep(0.2)

connect_wifi()
poll_server()

