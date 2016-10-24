import RPi._GPIO as GPIO
import time
import serial

# Setup Serial
port = serial.Serial("/dev/ttyAMA0", baudrate = 115200, timeout = 0)

#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# OE0 - H
# OE1 - L
# LE  - L

# A0 - GPIO 17
# A1 - GPIO 27
# A2 - GPIO 22

# Setup the Outputs
A0 = 17
A1 = 27
A2 = 22

GPIO.setup(A0, GPIO.OUT)
GPIO.setup(A1, GPIO.OUT)
GPIO.setup(A2, GPIO.OUT)

GPIO.output(A0, True)
GPIO.output(A1, True)
GPIO.output(A2, False)

time.sleep(1)

GPIO.output(A0, False)
GPIO.output(A1, False)
GPIO.output(A2, False)

while True:
	if(port.inWaiting() > 0):
		rcv = port.readline()
		print(rcv)
		break

time.sleep(1)

GPIO.output(A0, True)
GPIO.output(A1, False)
GPIO.output(A2, False)

while True:
	if(port.inWaiting() > 0):
		rcv = port.readline()
		print(rcv)
		break

time.sleep(1)

GPIO.output(A0, True)
GPIO.output(A1, True)
GPIO.output(A2, False)

while True:
	if(port.inWaiting() > 0):
		rcv = port.readline()
		print(rcv)
		break