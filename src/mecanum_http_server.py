import network
import socket
import utime
from machine import I2C, Pin
from Makerlab_I2C_Motor_Driver import Makerlabvn_I2C_Motor_Driver

WIFI_SSID = "Dngvmnh"
WIFI_PASS = "Persistent2025"

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

per = 100  

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

def turn_left():
    stop()
    utime.sleep(0.1)
    print("Turning Left")
    motor_driver_0.writeMA(0, per)
    motor_driver_0.writeMB(1, per)
    motor_driver_1.writeMC(0, per)
    motor_driver_1.writeMD(1, per)

def turn_right():
    stop()
    utime.sleep(0.1)
    print("Turning Right")
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

def execute_command(command):
    function_map = {
        "forward": forward,
        "backward": backward,
        "left": turn_left,
        "right": turn_right,
        "stop": stop
    }

    if command in function_map:
        function_map[command]()
    else:
        print("Invalid command:", command)

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
    <p><strong>Use arrow keys or buttons to move. Release to stop.</strong></p>
    
    <button onclick="sendCommand('diagonal-left')">Diagonal Left</button>
    <button onclick="sendCommand('forward')">Forward</button>
    <button onclick="sendCommand('diagonal-right')">Diagonal Right</button><br>
    
    <button onclick="sendCommand('left')">Move Left</button>
    <button onclick="sendCommand('stop')">Stop</button>
    <button onclick="sendCommand('right')">Move Right</button><br>
    
    <button onclick="sendCommand('concern-left')">Concern Left</button>
    <button onclick="sendCommand('backward')">Backward</button>
    <button onclick="sendCommand('concern-right')">Concern Right</button>

    <script>
        let activeKeys = {};

        function sendCommand(command) {
            fetch('/' + command)
                .then(response => console.log('Command sent:', command))
                .catch(error => console.error('Error sending command:', error));
        }

        document.addEventListener("keydown", function(event) {
            if (!activeKeys[event.key]) {  
                activeKeys[event.key] = true;  
                switch(event.key) {
                    case "ArrowUp":
                        sendCommand("forward");
                        break;
                    case "ArrowDown":
                        sendCommand("backward");
                        break;
                    case "ArrowLeft":
                        sendCommand("left");
                        break;
                    case "ArrowRight":
                        sendCommand("right");
                        break;
                    case "q":
                        sendCommand("diagonal-left");
                        break;
                    case "e":
                        sendCommand("diagonal-right");
                        break;
                    case "a":
                        sendCommand("concern-left");
                        break;
                    case "d":
                        sendCommand("concern-right");
                        break;
                }
            }
        });

        document.addEventListener("keyup", function(event) {
            if (activeKeys[event.key]) {  
                delete activeKeys[event.key];  
                sendCommand("stop");
            }
        });
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

    command = request_str.split("GET /")[1].split(" ")[0]
    execute_command(command)  

    conn.send("HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n")
    conn.sendall(html)
    conn.close()


