 🛠 1. ESP32 Mecanum Vehicle Control via Flask

This guide sets up a remote control system for an ESP32 Mecanum vehicle using a Flask web interface hosted on a computer. Commands are sent over Wi-Fi and executed by the ESP32.


🌐 2. Configure Windows Firewall (Allow Flask Port)

To allow external devices (ESP32) to access your Flask server, run this command in **Command Prompt (as Administrator)**:

netsh advfirewall firewall add rule name="Flask Port 5000" dir=in action=allow protocol=TCP localport=5000

💻 3. Flask Web Server (Computer Side)
This Python app provides a browser interface and keyboard input control to send movement commands to the ESP32.

➕ Features
User-friendly HTML interface with buttons and keyboard control

Sends commands like forward, left, stop, etc.

RESTful JSON interface for GET and POST on /command

📄 Flask App Code (save as flask_control.py)
python
Copy
Edit
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
command = {"action": "stop"}

@app.route('/')
def home():
    return render_template_string(html_interface)

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/command', methods=['GET'])
def get_command():
    return jsonify(command)

@app.route('/command', methods=['POST'])
def set_command():
    data = request.json
    if "action" in data:
        command["action"] = data["action"]
        return jsonify({"status": "ok", "received": command}), 200
    else:
        return jsonify({"error": "Missing action"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

Then, open http://<your_computer_ip>:5000 in a browser to access the control interface.

📶 4. ESP32 MicroPython Client
This MicroPython script runs on the ESP32. It connects to Wi-Fi, continuously polls the Flask server, and drives the motors accordingly.

📄 ESP32 Code Summary
Connects to Wi-Fi (SSID, PASSWORD)

Polls http://<flask_ip>:5000/command

Executes appropriate motor commands for received JSON action

Uses Makerlab I2C motor drivers at addresses 0x40, 0x41

⚠️ Replace SERVER_URL with your Flask server’s actual IP (e.g., <http://192.168.1.100:5000/command>)

✅ Supported Commands
Command	Action
forward	Move forward
backward	Move backward
left	Move left (strafe)
right	Move right (strafe)
diagonal-left	Move diagonally to left
diagonal-right	Move diagonally to right
concern-left	Special turn left
concern-right	Special turn right
stop	Stop all movement
