import utime
import network
from machine import I2C, Pin
from Makerlab_I2C_Motor_Driver import Makerlabvn_I2C_Motor_Driver
import BlynkLib

WIFI_SSID = ""
WIFI_PASS = ""

BLYNK_TEMPLATE_ID = 'TMPL611Yft9gx'
BLYNK_TEMPLATE_NAME = 'Mecanum'
BLYNK_AUTH = 'YEqp8NOOGl5Ba5-rNcXRs35nZp07LzlR'

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)
    
    print("Connecting to WiFi", end="")
    while not wlan.isconnected():
        print(".", end="")
        utime.sleep(1)
    
    print("\nConnected to WiFi:", WIFI_SSID)
    print("IP Address:", wlan.ifconfig()[0])

connect_wifi()

blynk = BlynkLib.Blynk(BLYNK_AUTH)

i2c = I2C(1, scl=Pin(22), sda=Pin(21))
motor_driver_0 = Makerlabvn_I2C_Motor_Driver(i2c, 0x41)
motor_driver_1 = Makerlabvn_I2C_Motor_Driver(i2c, 0x40)
motor_driver_0.begin()
motor_driver_1.begin()

per = 50  

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

@blynk.VIRTUAL_WRITE(0)  # Forward (W)
def v0_handler(value):
    if int(value[0]) == 1:
        forward()
    else:
        stop()

@blynk.VIRTUAL_WRITE(1)  # Backward (S)
def v1_handler(value):
    if int(value[0]) == 1:
        backward()
    else:
        stop()

@blynk.VIRTUAL_WRITE(2)  # Left (A)
def v2_handler(value):
    if int(value[0]) == 1:
        turn_left()
    else:
        stop()

@blynk.VIRTUAL_WRITE(3)  # Right (D)
def v3_handler(value):
    if int(value[0]) == 1:
        turn_right()
    else:
        stop()

@blynk.VIRTUAL_WRITE(4)  # Stop (X)
def v4_handler(value):
    if int(value[0]) == 1:
        stop()

# Main loop
while True:
    blynk.run()
    utime.sleep(0.1)
