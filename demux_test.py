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
		GPIO.setup(A0Mux, GPIO.OUT)
		GPIO.setup(A1Mux, GPIO.OUT)
		GPIO.setup(muxEnable, GPIO.OUT)

		GPIO.setup(A0, GPIO.OUT)
		GPIO.setup(A1, GPIO.OUT)
		GPIO.setup(A2, GPIO.OUT)

		GPIO.output(muxEnable, False)

		thread2.start()
		time.sleep(2)
		
		print("Enable #1")
		GPIO.output(muxEnable, True)
		GPIO.output(A0Mux, False)
		GPIO.output(A1Mux, False)
		
		# 000
		GPIO.output(A0, False)
		GPIO.output(A1, False)
		GPIO.output(A2, False)

		time.sleep(1)

		#001
		GPIO.output(A0, True)
		GPIO.output(A1, False)
		GPIO.output(A2, False)


		time.sleep(1)

		#010
		GPIO.output(A0, False)
		GPIO.output(A1, True)
		GPIO.output(A2, False)


		time.sleep(1)

		#011
		GPIO.output(A0, True)
		GPIO.output(A1, True)
		GPIO.output(A2, False)

		time.sleep(1)

		#100
		GPIO.output(A0,False)
		GPIO.output(A1,False)
		GPIO.output(A2,True)

		time.sleep(1)

		#101
		GPIO.output(A0,True)
		GPIO.output(A1,False)
		GPIO.output(A2,True)

		time.sleep(1)

		#110
		GPIO.output(A0,False)
		GPIO.output(A1,True)
		GPIO.output(A2,True)

		time.sleep(1)

		#111
		GPIO.output(A0,True)
		GPIO.output(A1,True)
		GPIO.output(A2,True)

		time.sleep(2)
		
		print("Enable #2")
		GPIO.output(muxEnable, True)
		GPIO.output(A0Mux, True)
		GPIO.output(A1Mux, False)
		# 000
		GPIO.output(A0, False)
		GPIO.output(A1, False)
		GPIO.output(A2, False)

		time.sleep(1)

		#001
		GPIO.output(A0, True)
		GPIO.output(A1, False)
		GPIO.output(A2, False)


		time.sleep(1)

		#010
		GPIO.output(A0, False)
		GPIO.output(A1, True)
		GPIO.output(A2, False)


		time.sleep(1)

		#011
		GPIO.output(A0, True)
		GPIO.output(A1, True)
		GPIO.output(A2, False)

		time.sleep(1)

		#100
		GPIO.output(A0,False)
		GPIO.output(A1,False)
		GPIO.output(A2,True)

		time.sleep(1)

		#101
		GPIO.output(A0,True)
		GPIO.output(A1,False)
		GPIO.output(A2,True)

		time.sleep(1)

		#110
		GPIO.output(A0,False)
		GPIO.output(A1,True)
		GPIO.output(A2,True)

		time.sleep(1)

		#111
		GPIO.output(A0,True)
		GPIO.output(A1,True)
		GPIO.output(A2,True)

		time.sleep(2)
		print("Enable #3")
		GPIO.output(muxEnable, True)
		GPIO.output(A0Mux, False)
		GPIO.output(A1Mux, True)

		# 000
		GPIO.output(A0, False)
		GPIO.output(A1, False)
		GPIO.output(A2, False)

		time.sleep(1)

		#001
		GPIO.output(A0, True)
		GPIO.output(A1, False)
		GPIO.output(A2, False)


		time.sleep(1)

		#010
		GPIO.output(A0, False)
		GPIO.output(A1, True)
		GPIO.output(A2, False)


		time.sleep(1)

		#011
		GPIO.output(A0, True)
		GPIO.output(A1, True)
		GPIO.output(A2, False)

		time.sleep(1)

		#100
		GPIO.output(A0,False)
		GPIO.output(A1,False)
		GPIO.output(A2,True)

		time.sleep(1)

		#101
		GPIO.output(A0,True)
		GPIO.output(A1,False)
		GPIO.output(A2,True)

		time.sleep(1)

		#110
		GPIO.output(A0,False)
		GPIO.output(A1,True)
		GPIO.output(A2,True)

		time.sleep(1)

		#111
		GPIO.output(A0,True)
		GPIO.output(A1,True)
		GPIO.output(A2,True)
		time.sleep(2)

		print("Enable #4")
		GPIO.output(muxEnable, True)
		GPIO.output(A0Mux, True)
		GPIO.output(A1Mux, True)

		# 000
		GPIO.output(A0, False)
		GPIO.output(A1, False)
		GPIO.output(A2, False)

		time.sleep(1)

		#001
		GPIO.output(A0, True)
		GPIO.output(A1, False)
		GPIO.output(A2, False)


		time.sleep(1)

		#010
		GPIO.output(A0, False)
		GPIO.output(A1, True)
		GPIO.output(A2, False)


		time.sleep(1)

		#011
		GPIO.output(A0, True)
		GPIO.output(A1, True)
		GPIO.output(A2, False)

		time.sleep(1)

		#100
		GPIO.output(A0,False)
		GPIO.output(A1,False)
		GPIO.output(A2,True)

		time.sleep(1)

		#101
		GPIO.output(A0,True)
		GPIO.output(A1,False)
		GPIO.output(A2,True)

		time.sleep(1)

		#110
		GPIO.output(A0,False)
		GPIO.output(A1,True)
		GPIO.output(A2,True)

		time.sleep(1)

		#111
		GPIO.output(A0,True)
		GPIO.output(A1,True)
		GPIO.output(A2,True)
		time.sleep(2)

		GPIO.output(muxEnable, False)

		print("Test Completed!")
		q.put(_sentinel)


thread = testThread(q)
thread2 = printThread(q)

print("Start the Test Thread!")
thread.start()