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
GPIO.cleanup()
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
	encoderPinToggle()

def leftButtonsTest():
	consoleCommand("8")
	leftToeButtonsPress() 
	time.sleep(12)

def rightButtonsTest():
	consoleCommand("8")
	rightToeButtonsPress()
	time.sleep(12)

def powerButtonTest():
	consoleCommand("9")
	powerButtonPress()
	time.sleep(7)


def sdCardTest():
	consoleCommand("11")
	time.sleep(1)

def pingTest():
	consoleCommand("net_connect HUCKABEE2 thebatman WPA2")
	time.sleep(5)
	consoleCommand("net_ping 10.1.10.79")
	time.sleep(2)

def chargeTest():
	chargeOn()
	time.sleep(2)
	consoleCommand("16")
	time.sleep(2)
	chargeOff()



#Individual Tests


def muxSetup():
	GPIO.setup(A0Mux, GPIO.OUT)
	GPIO.setup(A1Mux, GPIO.OUT)
	GPIO.setup(muxEnable, GPIO.OUT)

	GPIO.setup(A0, GPIO.OUT)
	GPIO.setup(A1, GPIO.OUT)
	GPIO.setup(A2, GPIO.OUT)

def chargeOff():
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


def rightToeButtonsPress():
	GPIO.output(muxEnable, True)
	#110 - Right Leg 0
	GPIO.output(A0Mux, False)
	GPIO.output(A1Mux, True)
	GPIO.output(A0,False)
	GPIO.output(A1,True)
	GPIO.output(A2,True)

	time.sleep(1)

	#111 - Right Leg 1
	GPIO.output(A0Mux, False)
	GPIO.output(A1Mux, True)
	GPIO.output(A0,True)
	GPIO.output(A1,True)
	GPIO.output(A2,True)
	
	time.sleep(1)

	# 000 - Right Leg 2
	GPIO.output(A0Mux, True)
	GPIO.output(A1Mux, True)
	GPIO.output(A0, False)
	GPIO.output(A1, False)
	GPIO.output(A2, False)

	time.sleep(1)

	GPIO.output(muxEnable, False)

def leftToeButtonsPress():
	GPIO.output(muxEnable, True)
	#001 - Left Leg 0

	time.sleep(1)

	GPIO.output(A0Mux, True)
	GPIO.output(A1Mux, True)
	GPIO.output(A0, True)
	GPIO.output(A1, False)
	GPIO.output(A2, False)


	time.sleep(1)

	#010 - Left Leg 1
	GPIO.output(A0Mux, True)
	GPIO.output(A1Mux, True)
	GPIO.output(A0, False)
	GPIO.output(A1, True)
	GPIO.output(A2, False)


	time.sleep(1)

	#011 - Left Leg 2
	GPIO.output(A0Mux, True)
	GPIO.output(A1Mux, True)
	GPIO.output(A0, True)
	GPIO.output(A1, True)
	GPIO.output(A2, False)

	time.sleep(1)

	GPIO.output(muxEnable, False)


def powerButtonPress():
	GPIO.output(muxEnable, True)
	#100 - Power Button
	GPIO.output(A0Mux, True)
	GPIO.output(A1Mux, True)
	GPIO.output(A0,True)
	GPIO.output(A1,False)
	GPIO.output(A2,False)

	time.sleep(1)

	GPIO.output(muxEnable, False)

def encoderPinToggle():
	print("Encoder #0")
	GPIO.output(muxEnable, True)
	GPIO.output(A0Mux, False)
	GPIO.output(A1Mux, False)

	# 000 - Encoder 0, Bit 0
	GPIO.output(A0, False)
	GPIO.output(A1, False)
	GPIO.output(A2, False)

	time.sleep(1)

	#001 - Encoder 0, Bit 1
	GPIO.output(A0, True)
	GPIO.output(A1, False)
	GPIO.output(A2, False)


	time.sleep(1)

	#010 - Encoder 0, Bit 2
	GPIO.output(A0, False)
	GPIO.output(A1, True)
	GPIO.output(A2, False)


	time.sleep(1)

	#011 - Encoder 0, Bit 3
	GPIO.output(A0, True)
	GPIO.output(A1, True)
	GPIO.output(A2, False)

	time.sleep(1)

	print("Encoder #1")
	#100 - Encoder 1, Bit 0
	GPIO.output(A0,False)
	GPIO.output(A1,False)
	GPIO.output(A2,True)

	time.sleep(1)

	#101 - Encoder 1, Bit 1
	GPIO.output(A0,True)
	GPIO.output(A1,False)
	GPIO.output(A2,True)

	time.sleep(1)

	#110 - Encoder 1, Bit 2
	GPIO.output(A0,False)
	GPIO.output(A1,True)
	GPIO.output(A2,True)

	time.sleep(1)

	#111 - Encoder 1, Bit 3
	GPIO.output(A0,True)
	GPIO.output(A1,True)
	GPIO.output(A2,True)

	time.sleep(2)
	
	print("Encoder #2")
	GPIO.output(A0Mux, True)
	GPIO.output(A1Mux, False)
	# 000 - Encoder 2, Bit 0
	GPIO.output(A0, False)
	GPIO.output(A1, False)
	GPIO.output(A2, False)

	time.sleep(1)

	#001 - Encoder 2, Bit 1
	GPIO.output(A0, True)
	GPIO.output(A1, False)
	GPIO.output(A2, False)


	time.sleep(1)

	#010 - Encoder 2, Bit 2
	GPIO.output(A0, False)
	GPIO.output(A1, True)
	GPIO.output(A2, False)


	time.sleep(1)

	#011 - Encoder 2, Bit 3
	GPIO.output(A0, True)
	GPIO.output(A1, True)
	GPIO.output(A2, False)

	time.sleep(1)

	print("Encoder #3")
	#100 - Encoder 3, Bit 0
	GPIO.output(A0,False)
	GPIO.output(A1,False)
	GPIO.output(A2,True)

	time.sleep(1)

	#101 - Encoder 3, Bit 1
	GPIO.output(A0,True)
	GPIO.output(A1,False)
	GPIO.output(A2,True)

	time.sleep(1)

	#110 - Encoder 3, Bit 2
	GPIO.output(A0,False)
	GPIO.output(A1,True)
	GPIO.output(A2,True)

	time.sleep(1)

	#111 - Encoder 3, Bit 3
	GPIO.output(A0,True)
	GPIO.output(A1,True)
	GPIO.output(A2,True)

	time.sleep(2)

	print("Encoder #4")
	GPIO.output(muxEnable, True)
	GPIO.output(A0Mux, False)
	GPIO.output(A1Mux, True)

	# 000 - Encoder 4 - Bit 0
	GPIO.output(A0, False)
	GPIO.output(A1, False)
	GPIO.output(A2, False)

	time.sleep(1)

	#001 - Encoder 4, Bit 1
	GPIO.output(A0, True)
	GPIO.output(A1, False)
	GPIO.output(A2, False)


	time.sleep(1)

	#010 - Encoder 4, Bit 2
	GPIO.output(A0, False)
	GPIO.output(A1, True)
	GPIO.output(A2, False)


	time.sleep(1)

	#011 - Encoder 4, Bit 3
	GPIO.output(A0, True)
	GPIO.output(A1, True)
	GPIO.output(A2, False)

	time.sleep(1)

	#100 - Encoder 5, Bit 0
	GPIO.output(A0,False)
	GPIO.output(A1,False)
	GPIO.output(A2,True)

	time.sleep(1)

	#101 - Encoder 5, Bit 1
	GPIO.output(A0,True)
	GPIO.output(A1,False)
	GPIO.output(A2,True)

	time.sleep(1)

	GPIO.output(muxEnable, False)

def consoleCommand(commandString):
	port.write(commandString + "\r\n")
	port.flush()
	print("Issued command string: \n" + commandString)


# funkList = [[sdCardTest, "\n*****SD Card Test*****\n"], \
# 	    [leftButtonsTest, "\n*****Left Buttons Test*****\n"], \
# 	    [rightButtonsTest, "\n*****Right Buttons Test*****\n"], \
# 	    [powerButtonTest, "\n*****Power Buttons Test*****\n"], \
# 	    [ledTest, "\n*****LED Test*****\n"], \
# 	    [pingTest, "\n*****Ping Test*****\n"], \
# 	    [playTest, "\n*****Play Buttons Test*****\n"], \
# 	    [recordTest, "\n*****Record Buttons Test*****\n"], \
# 	    [playbackTest, "\n*****Playback Buttons Test*****\n"]]
funkList = [[leftButtonsTest, "\n*****Left Buttons Test*****\n"]]


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
				print("[ELFKIN OUTPUT] " + rcv)
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
		muxSetup()

		while(1):
			print("\n\n*******************************")
			print("[FCT TEST] Starting Test Suite!")
			print("*******************************")
			for test in funkList:
				raw_input(test[1]+ "Press Enter to continue...\n")
				test[0]()
			
			#q.put(_sentinel)

	
thread = testThread(q)
thread2 = printThread(q)

print("Start the Test Thread!")
thread.start()
thread2.start()
