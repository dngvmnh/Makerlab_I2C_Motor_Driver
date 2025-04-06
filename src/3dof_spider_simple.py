from machine import Pin, PWM
from time import sleep

servo_pins = [19, 23, 5, 13, 2, 14, 27, 26]
base_angles = [90, 60, 50, 90, 80, 80, 80, 80]

servos = [PWM(Pin(pin), freq=50) for pin in servo_pins]

S1, S2, S3, S4, S5, S6, S7, S8 = 0, 1, 2, 3, 4, 5, 6, 7

sleep_time = 0.1
crawl_speed_wait_time = 0.005
crawl_speed = 0.005

def base():
    for i in range(8):
        servos[i].duty(base_angles[i]) 

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
    
def move_servo_range(servo_index, start, end, step=1):
    for angle in range(start, end, step):
        servos[servo_index].duty(angle)
        sleep(crawl_speed)

def forward_R():
    base()

    move_servo_range(S6, base_angles[S6], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S4, base_angles[S4], 111)
    sleep(crawl_speed_wait_time)

    move_servo_range(S6, 101, base_angles[S6], -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S7, base_angles[S7], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S1, base_angles[S1], 71, -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S6, 101, base_angles[S6], -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S8, base_angles[S8], 101)
    move_servo_range(S5, base_angles[S5], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S4, 111, base_angles[S4], -1)
    move_servo_range(S1, 71, base_angles[S1])
    sleep(crawl_speed_wait_time)

    base()
    
def forward_L():
    base()

    move_servo_range(S5, base_angles[S5], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S2, base_angles[S2], 40, -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S5, 101, base_angles[S5], -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S8, base_angles[S8], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S3, base_angles[S3], 70)
    sleep(crawl_speed_wait_time)

    move_servo_range(S8, 101, base_angles[S8], -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S7, base_angles[S7], 101)
    move_servo_range(S6, base_angles[S6], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S2, 41, base_angles[S2])
    move_servo_range(S3, 71, base_angles[S3], -1)
    sleep(crawl_speed_wait_time)

    base()

def forward():
    forward_R()
    forward_L()
    
def backward_R():
    base()

    move_servo_range(S6, base_angles[S6], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S4, base_angles[S4], 70, -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S6, 101, base_angles[S6], -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S7, base_angles[S7], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S1, base_angles[S1], 111)
    sleep(crawl_speed_wait_time)

    move_servo_range(S7, 101, base_angles[S7], -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S8, base_angles[S8], 101)
    move_servo_range(S5, base_angles[S5], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S4, 71, base_angles[S4])
    move_servo_range(S1, 111, base_angles[S1], -1)
    sleep(crawl_speed_wait_time)

    base()
  
def backward_L():
    base()

    move_servo_range(S5, base_angles[S5], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S2, base_angles[S2], 81)
    sleep(crawl_speed_wait_time)

    move_servo_range(S5, 101, base_angles[S5], -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S8, base_angles[S8], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S3, base_angles[S3], 30, -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S8, 101, base_angles[S8], -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S7, base_angles[S7], 101)
    move_servo_range(S6, base_angles[S6], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S2, 81, base_angles[S2], -1)
    move_servo_range(S3, 31, base_angles[S3])
    sleep(crawl_speed_wait_time)

    base()

def backward():
    backward_R()
    backward_L()
    
def turn_left():
    base()

    move_servo_range(S6, base_angles[S6], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S4, base_angles[S4], 111)
    sleep(crawl_speed_wait_time)

    move_servo_range(S6, 101, base_angles[S6], -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S7, base_angles[S7], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S1, base_angles[S1], 111)
    sleep(crawl_speed_wait_time)

    move_servo_range(S7, 101, base_angles[S7], -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S8, base_angles[S8], 101)
    move_servo_range(S5, base_angles[S5], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S4, 111, base_angles[S4], -1)
    move_servo_range(S1, 111, base_angles[S1], -1)
    sleep(crawl_speed_wait_time)

    base()

def turn_right():
    base()

    move_servo_range(S5, base_angles[S5], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S2, base_angles[S2], 40, -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S5, 101, base_angles[S5], -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S8, base_angles[S8], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S3, base_angles[S3], 30, -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S8, 101, base_angles[S8], -1)
    sleep(crawl_speed_wait_time)

    move_servo_range(S7, base_angles[S7], 101)
    move_servo_range(S6, base_angles[S6], 101)
    sleep(crawl_speed_wait_time)

    move_servo_range(S2, 41, base_angles[S2])
    move_servo_range(S3, 31, base_angles[S3])
    sleep(crawl_speed_wait_time)

    base()

test_bot()
for i in range(10):
    forward()
    backward()
    turn_left()
    turn_right()
    sleep(crawl_speed_wait_time)
base()    




