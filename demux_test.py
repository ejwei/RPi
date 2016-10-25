import RPi._GPIO as GPIO
import time
import serial
import threading

# Setup Serial
port = serial.Serial("/dev/ttyAMA0", baudrate = 115200, timeout = none)

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

testComplete = 0

def printThread():
	while True:
		rcv = port.read()
		print(rcv)
		if (testComplete == 0): break

def testThread():
	GPIO.setup(A0, GPIO.OUT)
	GPIO.setup(A1, GPIO.OUT)
	GPIO.setup(A2, GPIO.OUT)
	
	thread2.start()
	time.sleep(5)


	GPIO.output(A0, False)
	GPIO.output(A1, False)
	GPIO.output(A2, False)

	time.sleep(5)

	GPIO.output(A0, True)
	GPIO.output(A1, False)
	GPIO.output(A2, False)

	time.sleep(5)

	GPIO.output(A0, True)
	GPIO.output(A1, True)
	GPIO.output(A2, False)

	port.close()

	print("Test Completed!")
	testComplete = 1

thread = threading.Thread(target=testThread)
thread2 = threading.Thread(target=printThread)
thread.start()