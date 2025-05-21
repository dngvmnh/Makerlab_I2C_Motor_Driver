import network
import socket
import utime
import json
from machine import I2C, Pin
from Makerlab_I2C_Motor_Driver_Lib import Makerlabvn_I2C_Motor_Driver

WIFI_SSID = "Dngvmnh"
WIFI_PASS = "Persistent2025"

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)

    print("Connecting to WiFi", end="")
    while not wlan.isconnected():
        print(".", end="")
        utime.sleep(1)

    print("\nConnected! IP:", wlan.ifconfig()[0])

connect_wifi()

i2c = I2C(1, scl=Pin(8), sda=Pin(9))
motor_driver_0 = Makerlabvn_I2C_Motor_Driver(i2c, 0x41)
motor_driver_1 = Makerlabvn_I2C_Motor_Driver(i2c, 0x40)
motor_driver_0.begin()
motor_driver_1.begin()

per = 75

def forward():
    stop()
    utime.sleep(0.1)
    print("Moving Forward")
    motor_driver_0.writeMA(1, per)
    motor_driver_0.writeMB(1, per)
    motor_driver_1.writeMC(1, per)
    motor_driver_1.writeMD(1, per)

def backward():
    stop()
    utime.sleep(0.1)
    print("Moving Backward")
    motor_driver_0.writeMA(0, per)
    motor_driver_0.writeMB(0, per)
    motor_driver_1.writeMC(0, per)
    motor_driver_1.writeMD(0, per)

def move_left():
    stop()
    utime.sleep(0.1)
    print("Moving Left")
    motor_driver_0.writeMA(0, per)
    motor_driver_0.writeMB(1, per)
    motor_driver_1.writeMC(1, per)
    motor_driver_1.writeMD(0, per)

def move_right():
    stop()
    utime.sleep(0.1)
    print("Moving Right")
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

def diagonal_left():
    stop()
    utime.sleep(0.1)
    print("Diagonal Left")
    motor_driver_0.writeMB(1, per)
    motor_driver_1.writeMC(1, per)

def diagonal_right():
    stop()
    utime.sleep(0.1)
    print("Diagonal Right")
    motor_driver_0.writeMA(1, per)
    motor_driver_1.writeMD(1, per)

def concern_left():
    stop()
    utime.sleep(0.1)
    print("Concern Left")
    motor_driver_0.writeMA(0, per)
    motor_driver_1.writeMD(0, per)

def concern_right():
    stop()
    utime.sleep(0.1)
    print("Concern Right")
    motor_driver_0.writeMB(0, per)
    motor_driver_1.writeMC(0, per)

def execute_command(command):
    function_map = {
        "forward": forward,
        "backward": backward,
        "left": move_left,
        "right": move_right,
        "stop": stop,
        "diagonal-left": diagonal_left,
        "diagonal-right": diagonal_right,
        "concern-left": concern_left,
        "concern-right": concern_right
    }

    if command in function_map:
        function_map[command]()
        return {"status": "success", "command": command}
    else:
        return {"status": "error", "message": "Invalid command"}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 80))
server_socket.listen(5)
print("API Server running...")

while True:
    conn, addr = server_socket.accept()
    request = conn.recv(1024)
    request_str = request.decode('utf-8')
    print(f"Request from {addr}: {request_str}")

    try:
        request_path = request_str.split("GET /")[1].split(" ")[0]
        command = request_path.split("?")[0] 
        response_data = execute_command(command)
    except Exception as e:
        response_data = {"status": "error", "message": str(e)}

    response_json = json.dumps(response_data)
    conn.send("HTTP/1.1 200 OK\nContent-Type: application/json\nConnection: close\n\n" + response_json)
    conn.close()
