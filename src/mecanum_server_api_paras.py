import network
import socket
import utime
import json
from machine import I2C, Pin
from Makerlab_I2C_Motor_Driver import Makerlabvn_I2C_Motor_Driver

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

i2c = I2C(1, scl=Pin(22), sda=Pin(21))
motor_driver_0 = Makerlabvn_I2C_Motor_Driver(i2c, 0x41)
motor_driver_1 = Makerlabvn_I2C_Motor_Driver(i2c, 0x40)
motor_driver_0.begin()
motor_driver_1.begin()

def forward(speed):
    stop()
    utime.sleep(0.1)
    print(f"Moving Forward at {speed}% speed")
    motor_driver_0.writeMA(1, speed)
    motor_driver_0.writeMB(1, speed)
    motor_driver_1.writeMC(1, speed)
    motor_driver_1.writeMD(1, speed)

def backward(speed):
    stop()
    utime.sleep(0.1)
    print(f"Moving Backward at {speed}% speed")
    motor_driver_0.writeMA(0, speed)
    motor_driver_0.writeMB(0, speed)
    motor_driver_1.writeMC(0, speed)
    motor_driver_1.writeMD(0, speed)

def move_left(speed):
    stop()
    utime.sleep(0.1)
    print(f"Moving Left at {speed}% speed")
    motor_driver_0.writeMA(0, speed)
    motor_driver_0.writeMB(1, speed)
    motor_driver_1.writeMC(1, speed)
    motor_driver_1.writeMD(0, speed)

def move_right(speed):
    stop()
    utime.sleep(0.1)
    print(f"Moving Right at {speed}% speed")
    motor_driver_0.writeMA(1, speed)
    motor_driver_0.writeMB(0, speed)
    motor_driver_1.writeMC(0, speed)
    motor_driver_1.writeMD(1, speed)

def stop():
    print("Stopped")
    motor_driver_0.writeMA(0, 0)
    motor_driver_0.writeMB(0, 0)
    motor_driver_1.writeMC(0, 0)
    motor_driver_1.writeMD(0, 0)

def execute_command(data):
    try:
        command = data.get("direction")
        duration = float(data.get("time", 1))  
        speed = int(data.get("speed", 75))     

        function_map = {
            "forward": forward,
            "backward": backward,
            "left": move_left,
            "right": move_right
        }

        if command in function_map:
            function_map[command](speed)
            utime.sleep(duration)  
            stop() 
            return {"status": "success", "command": command, "time": duration, "speed": speed}
        else:
            return {"status": "error", "message": "Invalid command"}

    except Exception as e:
        return {"status": "error", "message": str(e)}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 80))
server_socket.listen(5)
print("API Server running...")

while True:
    conn, addr = server_socket.accept()
    request = conn.recv(1024).decode('utf-8')
    print(f"Request from {addr}: {request}")

    try:
        request_body = request.split("\r\n\r\n")[-1]  
        request_data = json.loads(request_body)
        response_data = execute_command(request_data)
    except Exception as e:
        response_data = {"status": "error", "message": str(e)}

    response_json = json.dumps(response_data)
    conn.send("HTTP/1.1 200 OK\nContent-Type: application/json\nConnection: close\n\n" + response_json)
    conn.close()
