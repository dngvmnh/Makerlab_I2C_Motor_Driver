from time import sleep
import math

servo_pins = [19, 23, 5, 13, 2, 14, 27, 26]
base_angles = [90, 60, 50, 90, 80, 80, 80, 80]
S1, S2, S3, S4, S5, S6, S7, S8 = 0, 1, 2, 3, 4, 5, 6, 7
sleep_time = 0.1
crawl_speed_wait_time = 0.005
crawl_speed = 0.005
L1 = 4  # femur
L2 = 5  # tibia 
corner_1 = (-2.5, -4, 0)
corner_2 = (-2.5, 4, 0)
corner_3 = (2.5, -4, 0)
corner_4 = (2.5, 4, 0)

from machine import Pin, PWM
servos = [PWM(Pin(pin), freq=50) for pin in servo_pins]
crawl_speed = 0.005
def base():
    for i in range(8):
        servos[i].duty(base_angles[i]) 
def move_servo_range(servo_index, start, end, step=1):
    for angle in range(start, end, step):
        servos[servo_index].duty(angle)
        sleep(crawl_speed)

def ik_theta(x, y, z, corner):    
    dx, dy, dz = x - corner[0], y - corner[1], z - corner[2]
    L3 = math.sqrt(dx**2 + dy**2 + dz**2)
    if abs(L3) > (L1 + L2) or abs(L3) < abs(L1 - L2):
        print("Error: leg out of reach")
        return None
    L4 = math.sqrt(L2**2 -z **2)
    cos_theta2 = (L1**2 + L2**2 - L3**2)/(2 * L1 * L2)
    theta2 = math.acos(cos_theta2)
    theta2 = math.degrees(theta2)
    theta1 = math.acos(y/(L1 + L4))
    theta1 = math.degrees(theta1)
    while theta1 > 90:
        theta1 = 180 - theta1
    while theta1 < 0:
        theta1 = 180 + theta1
    while theta2 > 90:
        theta2 = 180 - theta2
    while theta2 < 0:
        theta2 = 180 + theta2
    # if 15 < theta1 < 75 or 60 < theta2 < 100:
    #     print("Error: angles out of range")
    #     return None
    theta1 = max(15, min(theta1, 75))
    theta2 = max(60, min(theta2, 100))
    return theta1, theta2

def tripod_step(step_size=1.0, lift_height=2.0, z_ground=0.0):
    default_positions = {
        's1': (-2.5, -4, z_ground),
        's2': (-2.5, 4, z_ground),
        's3': (2.5, -4, z_ground),
        's4': (2.5, 4, z_ground)
    }
    corners = {'s1': corner_1, 's2': corner_2, 's3': corner_3, 's4': corner_4}
    forward_offset = (0, step_size, 0)
    lift_offset = (0, 0, lift_height)
    tripod_legs = [['s4'], ['s1'], ['s3'],['s2']]
    for leg_group in tripod_legs:
        for leg in leg_group:
            x, y, z = default_positions[leg]

            # Lift leg
            lifted = (x + forward_offset[0], y + forward_offset[1], z + lift_offset[2])
            angles = ik_theta(*lifted, corners[leg])
            if angles:
                print(f"Move leg {leg} to {lifted} -> angles: {angles}")
                # servos[...] = duty based on angles

            # Lower leg forward
            forward = (x + forward_offset[0], y + forward_offset[1], z)
            angles = ik_theta(*forward, corners[leg])
            if angles:
                print(f"Place leg {leg} to {forward} -> angles: {angles}")
                # servos[...] = duty based on angles

        sleep(sleep_time)

tripod_step()