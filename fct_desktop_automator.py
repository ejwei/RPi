import time
import serial
import threading
import Queue 

# Setup Serial
port = serial.Serial("/dev/ttyUSB0", baudrate = 115200, timeout = None)
q = Queue.Queue(0)

# Object that signals shutdown
_sentinel = object()


#selftest commands

def ledTest():
	consoleCommand("led")
	time.sleep(10)

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

def sdCardTest():
	consoleCommand("11")
	time.sleep(1)

def pingTest():
	consoleCommand("net_connect HUCKABEE2 thebatman WPA2")
	time.sleep(5)
	consoleCommand("net_ping 10.1.10.79")
	time.sleep(2)

def leftButtonsTest():
	consoleCommand("8")
	time.sleep(15)

def rightButtonsTest():
	consoleCommand("8")
	time.sleep(15)

def powerButtonTest():
	consoleCommand("9")
	time.sleep(8)


def consoleCommand(commandString):
	port.write(commandString + "\r\n")
	port.flush()
	print("Issued command string: \n" + commandString)


#funkList = [ledTest, playTest, recordTest, playbackTest, motorTest, encoderTest, leftButtonTest, rightButtonTest, \
			# powerButtonTest, sdCardTest, pingTest, chargeTest]

funkList = [[sdCardTest, "\n*****SD Card Test*****\n"], \
	    [leftButtonsTest, "\n*****Left Buttons Test*****\n"], \
	    [rightButtonsTest, "\n*****Right Buttons Test*****\n"], \
	    [powerButtonTest, "\n*****Power Buttons Test*****\n"], \
	    [ledTest, "\n*****LED Test*****\n"], \
	    [pingTest, "\n*****Ping Test*****\n"], \
	    [playTest, "\n*****Play Buttons Test*****\n"], \
	    [recordTest, "\n*****Record Buttons Test*****\n"], \
	    [playbackTest, "\n*****Playback Buttons Test*****\n"]]

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
