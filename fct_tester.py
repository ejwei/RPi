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


numTests = 7

#selftest commands

def ledTest():
	consoleCommand("led")
	time.sleep(3)

def playTest():
	consoleCommand("play")
	time.sleep(2)

def recordTest():
	consoleCommand("record")
	time.sleep(6)

def playbackTest():
	consoleCommand("playback")
	time.sleep(6)

def motorTest():
	consoleCommand("6")
	time.sleep(3)

def encoderTest():
	consoleCommand("7")
	demuxTest()
	time.sleep(15)

def buttonTest():
	consoleCommand("8")
	time.sleep(3)

def powerButtonTest():
	consoleCommand("9")
	time.sleep(2)

def sdCardTest():
	consoleCommand("11")
	time.sleep(1)

def pingTest():
	consoleCommand("net_connect empathKY_FEP goldenbear WPA2")
	time.sleep(5)
	consoleCommand("net_ping 10.1.10.1")
	time.sleep(2)

def chargeTest():
	chargeOn()
	consoleCommand("16")
	time.sleep(1)
	chargeOff()



#Individual Tests

def chargeOff():
	GPIO.setup(A0Mux, GPIO.OUT)
	GPIO.setup(A1Mux, GPIO.OUT)
	GPIO.setup(muxEnable, GPIO.OUT)

	GPIO.setup(A0, GPIO.OUT)
	GPIO.setup(A1, GPIO.OUT)
	GPIO.setup(A2, GPIO.OUT)

	GPIO.output(muxEnable, False)

	time.sleep(2)

	print("Enable #4")
	GPIO.output(muxEnable, False)
	GPIO.output(A0Mux, True)
	GPIO.output(A1Mux, True)

	time.sleep(1)

	#101 (Y5)
	GPIO.output(A0,True)
	GPIO.output(A1,False)
	GPIO.output(A2,True)

	print("Charge Off!")

def chargeOn():
	GPIO.setup(A0Mux, GPIO.OUT)
	GPIO.setup(A1Mux, GPIO.OUT)
	GPIO.setup(muxEnable, GPIO.OUT)

	GPIO.setup(A0, GPIO.OUT)
	GPIO.setup(A1, GPIO.OUT)
	GPIO.setup(A2, GPIO.OUT)

	GPIO.output(muxEnable, False)

	time.sleep(2)

	print("Enable #4")
	GPIO.output(muxEnable, True)
	GPIO.output(A0Mux, True)
	GPIO.output(A1Mux, True)

	time.sleep(1)

	#101 (Y5)
	GPIO.output(A0,True)
	GPIO.output(A1,False)
	GPIO.output(A2,True)

	print("Charge On!")

def demuxTest():
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




def consoleCommand(commandString):
	port.write(commandString + "\r\n")
	port.flush()
	print("Issued command string: \n" + commandString)


#funkList = [ledTest, playTest, recordTest, playbackTest, motorTest, encoderTest, buttonTest, buttonTest, \
#			 powerButtonTest, sdCardTest, pingTest, chargeTest]

funkList = [ledTest, sdCardTest, pingTest, chargeTest]

class printThread(threading.Thread):
	def __init__(self, q):
		self.q = q
		threading.Thread.__init__ (self)

	def run(self):
		while True:
			bytesToRead = port.inWaiting()

			if(bytesToRead > 0):
				# print("Reading Bytes")
				rcv = port.readline()
				# rcv = port.read(bytesToRead)
				print("[ELFKIN OUTPUT]" + rcv)
				# print("Done with Bytes")

			if not q.empty():
				print("Closing the Thread")
				port.close()
				break

class testThread(threading.Thread):
	def __init__(self, q):
		self.q = q
		threading.Thread.__init__ (self)

	def run(self):

		while(1):

			print("*******************************")
			print("[FCT TEST] Starting Test Suite!")
			print("*******************************")
			for test in funkList:
				raw_input("Press Enter to continue...")
				test()
			
			#q.put(_sentinel)

	
thread = testThread(q)
thread2 = printThread(q)

print("Start the Test Thread!")
thread.start()
thread2.start()
