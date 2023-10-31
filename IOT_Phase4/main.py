import machine
from machine import Pin,PWM
from time import sleep_us,sleep
from f import Servo
import hcsr04
import urequests
import os as MOD_OS
import network as MOD_NETWORK

#Connect to Wifi
GLOB_WLAN=MOD_NETWORK.WLAN(MOD_NETWORK.STA_IF)
GLOB_WLAN.active(True)
GLOB_WLAN.connect("Wokwi-GUEST", "")

while not GLOB_WLAN.isconnected():
  pass

# Firebase Realtime Database URL and secret
firebase_url = "https://ibmnm-2e8ff-default-rtdb.firebaseio.com/"

firebase_secret = '92CzMcbXSeaLMiHrvSMA8zhxtZre2Q2ORzlujqjD'

# Define the pins for the ultrasonic sensor and the LED
t1 = 0
e1 = 2
t2 = 4
e2 = 5
t3 = 16
e3 = 17
t4 = 18
e4 = 19
t5 = 21
e5 = 22
t6 = 25
e6 = 26
ser1 = 12
ser2 = 13
ser3 = 14
ser4 = 15
led1 = 32
led2 = 33
led3 = 27

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
detection_range = 250
l=["A1","A1","A3"]

def occup(led,ser,slot):
    led.on()
    Servo(0,ser)
    url = f'{firebase_url}/ibmnm.json?auth={firebase_secret}'
    data={slot:"Occupied"}
    response = urequests.patch(url, json=data)
    response.close()

def avail(led,ser,slot):
    led.off()
    Servo(90,ser)
    url = f'{firebase_url}/ibmnm.json?auth={firebase_secret}'
    data={slot:"Available"}
    response = urequests.patch(url, json=data)
    response.close()

def dist(usno):
    dis=usno.distance_cm()
    return dis

while True:

    occup(l1,ser2,"1") if dist(us1)<detection_range and dist(us2)<detection_range else avail(l1,ser2,"1")

    occup(l2,ser3,"2") if dist(us3)<detection_range and dist(us4)<detection_range else avail(l2,ser3,"2")

    occup(l3,ser4,"3") if dist(us5)<detection_range and dist(us6)<detection_range else avail(l3,ser4,"3")

    if dist(us1)<detection_range and dist(us2)<detection_range and dist(us3)<detection_range and dist(us4)<detection_range and dist(us5)<detection_range and dist(us6)<detection_range:
        Servo(0,ser1)