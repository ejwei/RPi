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
A0Mux = 4
A1Mux = 18
muxEnable = 25

A0 = 17
A1 = 27
A2 = 22


class printThread(threading.Thread):
	def __init__(self, q):
		self.q = q
		threading.Thread.__init__ (self)

	def run(self):
		while True:
			bytesToRead = port.inWaiting()

			if(bytesToRead > 0):
				print("Reading Bytes")
				rcv = port.readline()
				# rcv = port.read(bytesToRead)
				print(rcv)
				print("Done with Bytes")

			if not q.empty():
				print("Closing the Thread")
				port.close()
				break

class testThread(threading.Thread):
	def __init__(self, q):
		self.q = q
		threading.Thread.__init__ (self)

	def run(self):
		port.write("fg_read\r\n")
		port.flush()
		print("Test Completed!")
		q.put(_sentinel)


thread = testThread(q)
thread2 = printThread(q)

print("Start the Test Thread!")
thread.start()