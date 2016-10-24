import RPi._GPIO as GPIO
import time

#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# OE0 - H
# OE1 - L
# LE  - L

# A0 - GPIO 17
# A1 - GPIO 27
# A2 - GPIO 22

A0 = 17
A1 = 27
A2 = 22

GPIO.setup(A0, GPIO.OUT)
GPIO.setup(A1, GPIO.OUT)
GPIO.setup(A2, GPIO.OUT)

GPIO.output(A0, False)
GPIO.output(A1, False)
GPIO.output(A2, False)

time.sleep(1)

GPIO.output(A0, True)
GPIO.output(A1, False)
GPIO.output(A2, False)