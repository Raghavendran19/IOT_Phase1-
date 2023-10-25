import time
from machine import Pin,PWM
import hcsr04
import utime
from f import  Servo


# Define the pins for the ultrasonic sensor and the LED
t1 = 0
e1 = 1
t2 = 2
e2 = 3
t3 = 4
e3 = 5
t4 = 6
e4 = 7
t5 = 8
e5 = 9
t6 = 10
e6 = 11
ser1 = 12
ser2 = 13
ser3 = 14
ser4 = 15
led1 = 16
led2 = 17
led3 = 18

# Initialize the ultrasonic sensor
us1 = hcsr04.HCSR04(trigger_pin=t1, echo_pin=e1)
us2 = hcsr04.HCSR04(trigger_pin=t2, echo_pin=e2)
us3 = hcsr04.HCSR04(trigger_pin=t3, echo_pin=e3)
us4 = hcsr04.HCSR04(trigger_pin=t4, echo_pin=e4)
us5 = hcsr04.HCSR04(trigger_pin=t5, echo_pin=e5)
us6 = hcsr04.HCSR04(trigger_pin=t6, echo_pin=e6)

# Initialize the LED
l1 = Pin(led1, Pin.OUT)
l2 = Pin(led2, Pin.OUT)
l3 = Pin(led3, Pin.OUT)

# Initialize the servo
pwm1 = PWM(Pin(ser1), freq=50, duty=0)
pwm2 = PWM(Pin(ser2), freq=50, duty=0)
pwm3 = PWM(Pin(ser3), freq=50, duty=0)
pwm4 = PWM(Pin(ser4), freq=50, duty=0)

# Define the detection range (in centimeters)
detection_range = 250  # Adjust this value as needed

while True:
    distance1 = us1.distance_cm()
    distance2 = us2.distance_cm()
    distance3 = us3.distance_cm()
    distance4 = us4.distance_cm()
    distance5 = us5.distance_cm()
    distance6 = us6.distance_cm()
    
    if (distance1 < detection_range and distance2 < detection_range):
        l3.on()  # Turn on the LED
        Servo(pwm2, 0, ser2)
    else:
        l3.off()
        Servo(pwm2, 90, ser2)
        
    if (distance3 < detection_range and distance4 < detection_range):  
        l2.on()  # Turn on the LED
        Servo(pwm3, 0, ser3)
    else:
        l2.off()
        Servo(pwm3, 90, ser3)

    if (distance5 < detection_range and distance6 < detection_range):  
        l1.on()  # Turn on the LED
        Servo(pwm4, 0, ser4)
    else:
        l1.off()
        Servo(pwm4, 90, ser4)

    if (distance1 < detection_range and distance2 < detection_range and distance3 < detection_range and distance4 < detection_range and distance5 < detection_range and distance6 < detection_range):
        Servo(pwm1, 180, ser1)
    else:
        Servo(pwm1, 90, ser1)
