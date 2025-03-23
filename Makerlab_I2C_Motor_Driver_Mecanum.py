from machine import I2C, Pin
import time

class Makerlabvn_I2C_Motor_Driver:
    MAKERLABVN_I2C_DRIVER_SLAVE_ADDRESS_MIN = 0x10
    MAKERLABVN_I2C_DRIVER_SLAVE_ADDRESS_MAX = 0x7F
    DELAY_I2C_SEND = 0.02  # 20ms delay

    def __init__(self, i2c, address):
        self.i2c = i2c
        if address <= self.MAKERLABVN_I2C_DRIVER_SLAVE_ADDRESS_MAX:
            self.addressDriver = address
        else:
            self.addressDriver = self.MAKERLABVN_I2C_DRIVER_SLAVE_ADDRESS_MIN

    def begin(self):
        self.MA(0, 0)
        self.MB(0, 0)
        self.MC(0, 0)
        self.MD(0, 0)
        self.freeS1()
        self.freeS2()

    def checkSumCalculate(self, motor_data):
        tempSum = sum(motor_data)
        return tempSum & 0xFF  # Ensure it fits in a byte

    def scanI2CAddress(self):
        devices = self.i2c.scan()
        if len(devices) == 1:
            self.addressDriver = devices[0]
            return "I2C_MOTOR_DRIVER_CODE_SUCCESS"
        elif len(devices) > 1:
            return "I2C_MOTOR_DRIVER_CODE_MANY_CONNECT"
        return "I2C_MOTOR_DRIVER_CODE_NOT_CONNECT"

    def setAddress(self, address):
        if address <= self.MAKERLABVN_I2C_DRIVER_SLAVE_ADDRESS_MAX:
            self.addressDriver = address
            return "I2C_MOTOR_DRIVER_CODE_SUCCESS"
        return "I2C_MOTOR_DRIVER_CODE_INVALID_ADDRESS"

    def motorDC_Write(self, index, direction, speed):
        if index < 4:  # Now supporting 4 DC motors
            data = [self.addressDriver, 0x01, index, speed, direction]  # 0x01 is the mode ID
            data.append(self.checkSumCalculate(data))  # Add checksum
            self.i2c.writeto(self.addressDriver, bytes(data))
            time.sleep(self.DELAY_I2C_SEND)

    def motorRC_Write(self, index, pulse):
        if index < 4:  # Now supporting 4 RC motors
            data = [self.addressDriver, 0x02, index, pulse & 0xFF, (pulse >> 8) & 0xFF]
            data.append(self.checkSumCalculate(data))  # Add checksum
            self.i2c.writeto(self.addressDriver, bytes(data))
            time.sleep(self.DELAY_I2C_SEND)

    def MA(self, direction, speed):
        self.motorDC_Write(0, direction, speed)

    def MB(self, direction, speed):
        self.motorDC_Write(1, direction, speed)
    
    def MC(self, direction, speed):
        self.motorDC_Write(0, direction, speed)

    def MD(self, direction, speed):
        self.motorDC_Write(1, direction, speed)

    def writeMA(self, direction, percentSpeed):
        pwm = int((percentSpeed / 100) * 255)
        self.MA(direction, pwm)

    def writeMB(self, direction, percentSpeed):
        pwm = int((percentSpeed / 100) * 255)
        self.MB(direction, pwm)
    
    def writeMC(self, direction, percentSpeed):
        pwm = int((percentSpeed / 100) * 255)
        self.MC(direction, pwm)
    
    def writeMD(self, direction, percentSpeed):
        pwm = int((percentSpeed / 100) * 255)
        self.MD(direction, pwm)

    def freeS1(self):
        self.motorRC_Write(0, 0)

    def freeS2(self):
        self.motorRC_Write(1, 0)


