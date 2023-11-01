from machine import Pin, PWM
from time import sleep
import utime

# pwm


def Servo(angle,pin):
    pwm = PWM(Pin(pin), freq=50, duty=0)
    # angle / 180（ * 2（0°-180°） + 0.5（）/ 20ms * 1023
    pwm.duty(int(((angle)/180 *2 + 0.5) / 20 * 1023))    