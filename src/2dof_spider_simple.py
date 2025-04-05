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
crawl_speed_wait_time = 0.05
crawl_speed = 0.1

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
    
def forward_R():
    base()
    servos[S6].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S4].duty(110)
    sleep(crawl_speed_wait_time)
    servos[S6].duty(base_angles[S6])
    sleep(crawl_speed_wait_time)
    
    servos[S7].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S1].duty(70)
    sleep(crawl_speed_wait_time)
    servos[S7].duty(base_angles[S7])
    sleep(crawl_speed_wait_time)
    
    servos[S8].duty(100)
    servos[S5].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S4].duty(base_angles[S4])
    servos[S1].duty(base_angles[S1])
    sleep(crawl_speed_wait_time)
    base()
    
def forward_L():
    base()
    servos[S5].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S2].duty(40)
    sleep(crawl_speed_wait_time)
    servos[S5].duty(base_angles[S5])
    sleep(crawl_speed_wait_time)
    
    servos[S8].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S3].duty(70)
    sleep(crawl_speed_wait_time)
    servos[S8].duty(base_angles[S8])
    sleep(crawl_speed_wait_time)
    
    servos[S7].duty(100)
    servos[S6].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S2].duty(base_angles[S2])
    servos[S3].duty(base_angles[S3])
    sleep(crawl_speed_wait_time)
    base()
    
def forward():
    forward_R()
    forward_L()
    
def backward_R():
    base()
    servos[S6].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S4].duty(70)
    sleep(crawl_speed_wait_time)
    servos[S6].duty(base_angles[S6])
    sleep(crawl_speed_wait_time)
    
    servos[S7].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S1].duty(110)
    sleep(crawl_speed_wait_time)
    servos[S7].duty(base_angles[S7])
    sleep(crawl_speed_wait_time)
    
    servos[S8].duty(100)
    servos[S5].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S4].duty(base_angles[S4])
    servos[S1].duty(base_angles[S1])
    sleep(crawl_speed_wait_time)
    base()
    
def backward_L():
    base()
    servos[S5].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S2].duty(80)
    sleep(crawl_speed_wait_time)
    servos[S5].duty(base_angles[S5])
    sleep(crawl_speed_wait_time)
    
    servos[S8].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S3].duty(30)
    sleep(crawl_speed_wait_time)
    servos[S8].duty(base_angles[S8])
    sleep(crawl_speed_wait_time)
    
    servos[S7].duty(100)
    servos[S6].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S2].duty(base_angles[S2])
    servos[S3].duty(base_angles[S3])
    sleep(crawl_speed_wait_time)
    base()
    
def backward():
    backward_R()
    backward_L()
    
def turn_left():
    base()
    servos[S6].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S4].duty(110)
    sleep(crawl_speed_wait_time)
    servos[S6].duty(base_angles[S6])
    sleep(crawl_speed_wait_time)
    
    servos[S7].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S1].duty(110)
    sleep(crawl_speed_wait_time)
    servos[S7].duty(base_angles[S7])
    sleep(crawl_speed_wait_time)
    
    servos[S8].duty(100)
    servos[S5].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S4].duty(base_angles[S4])
    servos[S1].duty(base_angles[S1])
    sleep(crawl_speed_wait_time)
    base()
    
def turn_right():
    base()
    servos[S5].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S2].duty(40)
    sleep(crawl_speed_wait_time)
    servos[S5].duty(base_angles[S5])
    sleep(crawl_speed_wait_time)
    
    servos[S8].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S3].duty(30)
    sleep(crawl_speed_wait_time)
    servos[S8].duty(base_angles[S8])
    sleep(crawl_speed_wait_time)
    
    servos[S7].duty(100)
    servos[S6].duty(100)
    sleep(crawl_speed_wait_time)
    servos[S2].duty(base_angles[S2])
    servos[S3].duty(base_angles[S3])
    sleep(crawl_speed_wait_time)
    base()

test_bot()
for i in range(10):
    # forward()
    # backward()
    # turn_left()
    # turn_right()
    sleep(crawl_speed_wait_time)
base()    



