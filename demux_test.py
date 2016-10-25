import RPi._GPIO as GPIO
import time
import serial
import threading
import Queue 

# Setup Serial
port = serial.Serial("/dev/ttyAMA0", baudrate = 115200, timeout = None)
stringQueue = Queue.Queue(0)

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
		# print('Still in print thread')
		bytesToRead = port.inWaiting()
		if(bytesToRead > 0):
			print("Reading Bytes")
			rcv = port.read(bytesToRead)
			print(rcv)
			print("Done with Bytes")

		if (testComplete == 1): 
			print("Closing the Thread")
			port.close()
			thread2.exit()
			break

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

	time.sleep(5)

	print("Test Completed!")
	testComplete = 1
	print(testComplete)
	thread2.join()

thread = threading.Thread(target=testThread)
thread2 = threading.Thread(target=printThread)

thread.start()