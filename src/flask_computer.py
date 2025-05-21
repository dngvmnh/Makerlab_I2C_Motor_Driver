from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
command = {"action": "stop"}

html_interface = """
<!DOCTYPE html>
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
    <p style="text-align: left; display: inline-block; margin: 0 auto;">
        <strong>Control the movement of the mecanum vehicle using the arrow keys or on-screen buttons:</strong>
    </p><br>
    <ul style="text-align: left; display: inline-block; margin: 0 auto;">  
        <li>Press and hold the <strong>Up Arrow (↑)</strong> or click "Forward" to move forward.</li>  
        <li>Press and hold the <strong>Down Arrow (↓)</strong> or click "Backward" to move backward.</li>  
        <li>Press and hold the <strong>Left Arrow (←)</strong> or click "Move Left" to move left.</li>  
        <li>Press and hold the <strong>Right Arrow (→)</strong> or click "Move Right" to move right.</li>  
        <li>Press and hold the <strong>Q</strong> key or click "Diagonal Left" to move diagonally left.</li>  
        <li>Press and hold the <strong>E</strong> key or click "Diagonal Right" to move diagonally right.</li>  
        <li>Press and hold the <strong>A</strong> key or click "Concern Left" for a special left movement.</li>  
        <li>Press and hold the <strong>D</strong> key or click "Concern Right" for a special right movement.</li>  
        <li>Releasing any key will automatically stop the vehicle.</li>  
        <li>Click the "Stop" button to immediately halt all movement.</li>  
    </ul><br>
        
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
            fetch('/command', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ action: command })
            }).then(response => console.log('Sent:', command));
        }

        document.addEventListener("keydown", function(event) {
            if (!activeKeys[event.key]) {  
                activeKeys[event.key] = true;  
                switch(event.key) {
                    case "ArrowUp": sendCommand("forward"); break;
                    case "ArrowDown": sendCommand("backward"); break;
                    case "ArrowLeft": sendCommand("left"); break;
                    case "ArrowRight": sendCommand("right"); break;
                    case "q": sendCommand("diagonal-left"); break;
                    case "e": sendCommand("diagonal-right"); break;
                    case "a": sendCommand("concern-left"); break;
                    case "d": sendCommand("concern-right"); break;
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
