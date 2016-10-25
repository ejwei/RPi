import RPi._GPIO as GPIO
import time
import serial
import threading
import Queue 

# Setup Serial
port = serial.Serial("/dev/ttyAMA0", baudrate = 115200, timeout = None)
q = Queue.Queue(0)

# Object that signals shutdown
_sentinel = object()

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

class printThread(threading.Thread):
	def __init__(self, q):
		threading.Thread.__init__(self)
		self.q = q
		

	def run(self):
		while True:
			bytesToRead = port.inWaiting()

			if(bytesToRead > 0):
				print("Reading Bytes")
				rcv = port.read(bytesToRead)
				print(rcv)
				print("Done with Bytes")

			if(q.qsize() > 0): 
				print("Closing the Thread")
				port.close()
				thread2.exit()

class testThread(threading.Thread):
	
	def __init__(self, q):
		threading.Thread.__init__(self)
		self.q = q
		

	def run(self):
		GPIO.setup(A0, GPIO.OUT)
		GPIO.setup(A1, GPIO.OUT)
		GPIO.setup(A2, GPIO.OUT)
		
		thread2.start()
		time.sleep(0.1)
		
		GPIO.output(A0, False)
		GPIO.output(A1, False)
		GPIO.output(A2, False)

		time.sleep(0.1)

		GPIO.output(A0, True)
		GPIO.output(A1, False)
		GPIO.output(A2, False)

		time.sleep(0.1)

		GPIO.output(A0, True)
		GPIO.output(A1, True)
		GPIO.output(A2, False)

		time.sleep(0.1)

		print("Test Completed!")
		q.put(_sentinel)

thread = threading.Thread(target=testThread, args=(q,))
thread2 = threading.Thread(target=printThread, args=(q,))

thread.start()