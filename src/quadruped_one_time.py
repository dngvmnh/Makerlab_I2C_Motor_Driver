from machine import Pin, PWM
from time import sleep

# Map pins to servos
servo_pins = [19, 23, 5, 13, 2, 14, 27, 26]
servos = []

# Initialize PWM for each pin
for pin in servo_pins:
    pwm = PWM(Pin(pin), freq=50)
    servos.append(pwm)

# Convert angle to PWM duty (roughly for 0°–180°)
def angle_to_duty(angle):
    # Scale angle to duty (approx: 40 to 115)
    return int(40 + (angle / 180) * 75)

# Move all servos together from 70° to 80°
for angle in range(70, 81):  # 70° to 80° inclusive
    duty = angle_to_duty(angle)
    for servo in servos:
        servo.duty(duty)
    sleep(0.05)  # Small delay to smooth the movement
