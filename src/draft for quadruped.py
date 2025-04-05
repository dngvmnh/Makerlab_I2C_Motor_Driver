from machine import Pin, PWM
from time import sleep

# servo_pins = [19, 23, 5, 13, 2, 14, 27, 26]

for _ in range(0, 11):
# base 90
    s1=PWM(Pin(19), freq=50)
    s1.duty(70)
    sleep(1)
    s1.duty(110)
    sleep(1)

    # base 60
    s2=PWM(Pin(23), freq=50)
    s2.duty(80)
    sleep(1)
    s2.duty(40)
    sleep(1)

    # base 50
    s3=PWM(Pin(5), freq=50)
    s3.duty(70)
    sleep(1)
    s3.duty(30)
    sleep(1)

    # base 90
    s4=PWM(Pin(13), freq=50)
    s4.duty(70)
    sleep(1)
    s4.duty(110)
    sleep(1)

    # base 80
    s5=PWM(Pin(2), freq=50)
    s5.duty(60)
    sleep(1)
    s5.duty(100)
    sleep(1)

    # base 80
    s6=PWM(Pin(14), freq=50)
    s6.duty(60)
    sleep(1)
    s6.duty(100)
    sleep(1)

    # base 80
    s7=PWM(Pin(27), freq=50)
    s7.duty(60)
    sleep(1)
    s7.duty(100)
    sleep(1)

    # base 80
    s8=PWM(Pin(26), freq=50)
    s8.duty(60)
    sleep(1)
    s8.duty(100)
    sleep(1)

