import network
import socket
import utime
from machine import I2C, Pin
from Makerlab_I2C_Motor_Driver import Makerlabvn_I2C_Motor_Driver

WIFI_SSID = ""
WIFI_PASS = ""

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)

    print("Connecting to Wifi", end="")
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

per = 50

def forward():
    print("Forwarding")
    motor_driver_0.writeMA(1, per)
    motor_driver_0.writeMB(1, per)
    motor_driver_1.writeMC(1, per)
    motor_driver_1.writeMD(1, per)

def backward():
    print("Backwarding")
    motor_driver_0.writeMA(0, per)
    motor_driver_0.writeMB(0, per)
    motor_driver_1.writeMC(0, per)
    motor_driver_1.writeMD(0, per)

def turn_left():
    print("Turning Left")
    motor_driver_0.writeMA(0, per)
    motor_driver_0.writeMB(1, per)
    motor_driver_1.writeMC(0, per)
    motor_driver_1.writeMD(1, per)

def turn_right():
    print("Turining Right")
    motor_driver_0.writeMA(1, per)
    motor_driver_0.writeMB(0, per)
    motor_driver_1.writeMC(1, per)
    motor_driver_1.writeMD(0, per)

def stop():
    print("Stopped")
    motor_driver_0.writeMA(0, 0)
    motor_driver_0.writeMB(0, 0)
    motor_driver_1.writeMC(0, 0)
    motor_driver_1.writeMD(0, 0)

html = """<!DOCTYPE html>
<html>
<head>
    <title>ESP32 Mecanum</title>
    <style>
        body { text-align: center; font-family: Arial, sans-serif; }
        button { font-size: 20px; padding: 10px 20px; margin: 10px; }
    </style>
</head>
<body>
    <h2>Mecanum Control</h2>
    <button onclick="sendCommand('forward')">Forward</button><br>
    <button onclick="sendCommand('left')">Turn Left</button>
    <button onclick="sendCommand('stop')">Stop</button>
    <button onclick="sendCommand('right')">Turn Right</button><br>
    <button onclick="sendCommand('backward')">Backward</button>

    <script>
        function sendCommand(command) {
            fetch('/' + command)
                .then(response => console.log('Command sent:', command));
        }
    </script>
</body>
</html>
"""

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 80))
server_socket.listen(5)
print("HTTP Server running...")

while True:
    conn, addr = server_socket.accept()
    request = conn.recv(1024)
    request_str = request.decode('utf-8')
    print(f"Request from {addr}: {request_str}")

    if "/forward" in request_str:
        forward()
    elif "/backward" in request_str:
        backward()
    elif "/left" in request_str:
        turn_left()
    elif "/right" in request_str:
        turn_right()
    elif "/stop" in request_str:
        stop()

    conn.send("HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n")
    conn.sendall(html)
    conn.close()
