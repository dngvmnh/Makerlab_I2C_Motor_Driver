from machine import Pin, PWM
from time import sleep

servo_pins = [19, 23, 5, 13, 2, 14, 27, 26]
base_angles = [90, 60, 50, 90, 80, 80, 80, 80]

servos = [PWM(Pin(pin), freq=50) for pin in servo_pins]

S1 = 0
S2 = 1
S3 = 2
S4 = 3
S5 = 4
S6 = 5
S7 = 6
S8 = 7

sleep_time = 0.1

def base():
    for i in range(8):
        servos[i].duty(base_angles[i])
    sleep(1)  

def test_s1(sleep_time):
    s = PWM(Pin(19), freq=50)
    s.duty(70)
    sleep(sleep_time)
    s.duty(110)
    sleep(sleep_time)

def test_s2(sleep_time):
    s = PWM(Pin(23), freq=50)
    s.duty(80)
    sleep(sleep_time)
    s.duty(40)
    sleep(sleep_time)

def test_s3(sleep_time):
    s = PWM(Pin(5), freq=50)
    s.duty(70)
    sleep(sleep_time)
    s.duty(30)
    sleep(sleep_time)

def test_s4(sleep_time):
    s = PWM(Pin(13), freq=50)
    s.duty(70)
    sleep(sleep_time)
    s.duty(110)
    sleep(sleep_time)

def test_s5(sleep_time):
    s = PWM(Pin(2), freq=50)
    s.duty(60)
    sleep(sleep_time)
    s.duty(100)
    sleep(sleep_time)

def test_s6(sleep_time):
    s = PWM(Pin(14), freq=50)
    s.duty(60)
    sleep(sleep_time)
    s.duty(100)
    sleep(sleep_time)

def test_s7(sleep_time):
    s = PWM(Pin(27), freq=50)
    s.duty(60)
    sleep(sleep_time)
    s.duty(100)
    sleep(sleep_time)

def test_s8(sleep_time):
    s = PWM(Pin(26), freq=50)
    s.duty(60)
    sleep(sleep_time)
    s.duty(100)
    sleep(sleep_time)

def forward():
    base()
    servos[S4].duty(70)
    sleep(0.5)

    servos[S3].duty(30)
    sleep(0.5)

    servos[S4].duty(base_angles[S4])
    servos[S3].duty(base_angles[S3])
    sleep(0.5)

    servos[S2].duty(80)
    sleep(0.5)

    servos[S1].duty(110)
    sleep(0.5)

    servos[S2].duty(base_angles[S2])
    servos[S1].duty(base_angles[S1])
    sleep(0.5)

def backward():
    base()

    servos[S2].duty(40)  
    sleep(0.5)
    servos[S1].duty(70)  
    sleep(0.5)

    servos[S2].duty(base_angles[S2])
    servos[S1].duty(base_angles[S1])
    sleep(0.5)

    servos[S3].duty(70) 
    sleep(0.5)
    servos[S4].duty(110)  
    sleep(0.5)

    servos[S3].duty(base_angles[S3])
    servos[S4].duty(base_angles[S4])
    sleep(0.5)

def test_bot(): 
    base()
    test_s1(sleep_time)
    test_s2(sleep_time)
    test_s3(sleep_time)
    test_s4(sleep_time)
    test_s5(sleep_time)
    test_s6(sleep_time)
    test_s7(sleep_time)
    test_s8(sleep_time)

test_bot()
forward()
backward()
base()
    



