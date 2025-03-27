import requests

ESP32_IP = "192.168.161.168"  

def send_command(direction, time, speed):
    url = f"http://{ESP32_IP}/"
    data = {
        "direction": direction,
        "time": time,
        "speed": speed
    }
    response = requests.post(url, json=data)
    print(response.json())

send_command("forward", 3, 80)
send_command("backward", 2, 50)

# Send commands using CMD

# curl -X POST http://192.168.161.168/ ^
#      -H "Content-Type: application/json" ^
#      -d "{\"direction\": \"left\", \"time\": 5, \"speed\": 60}"

# Send commands using curl

# curl -X POST http://192.168.161.168/ \
#      -H "Content-Type: application/json" \
#      -d '{"direction": "left", "time": 5, "speed": 60}'
