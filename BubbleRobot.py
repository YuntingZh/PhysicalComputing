import time
import board
import analogio
import pwmio

from adafruit_motor import servo

analog_out = analogio.AnalogOut(board.A0)
analog_out.value = 45000
 
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)

while True:
    # run loop from 0 - 180 increase increments by 5
    for angle in range(0, 180, 3):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        print("angle:" + str(angle))
        if (angle >= 177):
            time.sleep(1.5)
            print("angle stop")
        time.sleep(0.01)
    for angle in range(180, 0, -3): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        print("angle:" + str(angle))
        time.sleep(0.01)
    time.sleep(0.01)
