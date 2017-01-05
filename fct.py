# Import standard Python time library.
import time

import sys
import serial

portName = "/dev/ttyACM0"

#Pin Positions in the GPIO extender
A0Mux = 5
A1Mux = 3
muxEnable = 0

A0 = 4
A1 = 2
A2 = 1

extender = serial.Serial(portName, 19200, timeout=1)

#These are the pins that we're using
enableThesePins = "003f"

#A 0 in the bit position indicates an output
ioDirMask = "0000"

#initial state for all pins
allPinsOff = "0000"

def configureGPIO():
	extender.write("gpio iomask "+ enableThesePins  + "\r")
	extender.write("gpio iodir "+ ioDirMask  + "\r")
	extender.write("gpio writeall "+ allPinsOff  + "\r")

def setGPIO(mask):
	maskStr = format(mask, '04x')
	extender.write("gpio writeall " + maskStr + "\r")

	print "Set GPIO mask to " + maskStr

def readAll():
	extender.write("gpio readall\r")
	response = extender.read(50)
	print response

def clearAllGPIO():
	extender.write("gpio writeall "+ allPinsOff  + "\r")

def powerButtonPress():
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 1 << A0Mux
	pinMask |= 1 << A1Mux
	pinMask |= 0 << A0
	pinMask |= 0 << A1
	pinMask |= 1 << A2

	setGPIO(pinMask)

	time.sleep(2)

	# readAll()
	clearAllGPIO()


def rightToeButtonsPress():
	#110 - Right Leg 0
	time.sleep(1)

	print("[FCT TESTER] R0 Button")
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 0 << A0Mux
	pinMask |= 1 << A1Mux
	pinMask |= 0 << A0
	pinMask |= 1 << A1
	pinMask |= 1 << A2
	setGPIO(pinMask)

	time.sleep(1)

	#111 - Right Leg 1
	print("[FCT TESTER] R1 Button")
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 0 << A0Mux
	pinMask |= 1 << A1Mux
	pinMask |= 1 << A0
	pinMask |= 1 << A1
	pinMask |= 1 << A2
	setGPIO(pinMask)
	
	time.sleep(1)

	# 000 - Right Leg 2
	print("[FCT TESTER] R2 Button")
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 1 << A0Mux
	pinMask |= 1 << A1Mux
	pinMask |= 0 << A0
	pinMask |= 0 << A1
	pinMask |= 0 << A2
	setGPIO(pinMask)

	time.sleep(1)

	clearAllGPIO()

def leftToeButtonsPress():
	#001 - Left Leg 0

	time.sleep(1)
	print("[FCT TESTER] L0 Button")
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 1 << A0Mux
	pinMask |= 1 << A1Mux
	pinMask |= 1 << A0
	pinMask |= 0 << A1
	pinMask |= 0 << A2
	setGPIO(pinMask)


	time.sleep(1)

	#010 - Left Leg 1
	print("[FCT TESTER] L1 Button")
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 1 << A0Mux
	pinMask |= 1 << A1Mux
	pinMask |= 0 << A0
	pinMask |= 1 << A1
	pinMask |= 0 << A2
	setGPIO(pinMask)

	time.sleep(1)

	#011 - Left Leg 2
	print("[FCT TESTER] L2 Button")
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 1 << A0Mux
	pinMask |= 1 << A1Mux
	pinMask |= 1 << A0
	pinMask |= 1 << A1
	pinMask |= 0 << A2
	setGPIO(pinMask)

	time.sleep(1)

	clearAllGPIO()

def powerMosfetOn():
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 1 << A0Mux
	pinMask |= 1 << A1Mux
	pinMask |= 1 << A0
	pinMask |= 0 << A1
	pinMask |= 1 << A2
	setGPIO(pinMask)


	print("Charge On!")

def powerMosfetOff():
	print("Charge Off!")
	clearAllGPIO()

def toggleEncoder0():
	print("Encoder #0")
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 0 << A0Mux
	pinMask |= 0 << A1Mux
	pinMask |= 0 << A0
	pinMask |= 0 << A1
	pinMask |= 0 << A2
	setGPIO(pinMask)

	time.sleep(1)

	# #001 - Encoder 0, Bit 1
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 0 << A0Mux
	pinMask |= 0 << A1Mux
	pinMask |= 1 << A0
	pinMask |= 0 << A1
	pinMask |= 0 << A2
	setGPIO(pinMask)

	time.sleep(1)

	#010 - Encoder 0, Bit 2
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 0 << A0Mux
	pinMask |= 0 << A1Mux
	pinMask |= 0 << A0
	pinMask |= 1 << A1
	pinMask |= 0 << A2
	setGPIO(pinMask)


	time.sleep(1)

	#011 - Encoder 0, Bit 3
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 0 << A0Mux
	pinMask |= 0 << A1Mux
	pinMask |= 1 << A0
	pinMask |= 1 << A1
	pinMask |= 0 << A2
	setGPIO(pinMask)

	time.sleep(1)
	clearAllGPIO()

def toggleEncoder1():
	print("Encoder #1")
	# #100 - Encoder 1, Bit 0
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 0 << A0Mux
	pinMask |= 0 << A1Mux
	pinMask |= 0 << A0
	pinMask |= 0 << A1
	pinMask |= 1 << A2
	setGPIO(pinMask)

	time.sleep(1)

	#101 - Encoder 1, Bit 1
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 0 << A0Mux
	pinMask |= 0 << A1Mux
	pinMask |= 1 << A0
	pinMask |= 0 << A1
	pinMask |= 1 << A2

	setGPIO(pinMask)

	time.sleep(1)

	# #110 - Encoder 1, Bit 2
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 0 << A0Mux
	pinMask |= 0 << A1Mux
	pinMask |= 0 << A0
	pinMask |= 1 << A1
	pinMask |= 1 << A2
	setGPIO(pinMask)

	time.sleep(1)

	#111 - Encoder 1, Bit 3
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 0 << A0Mux
	pinMask |= 0 << A1Mux
	pinMask |= 1 << A0
	pinMask |= 1 << A1
	pinMask |= 1 << A2
	setGPIO(pinMask)


	time.sleep(20)
	# clearAllGPIO()


def toggleEncoder2():
	print("Encoder #2")
	# # 000 - Encoder 2, Bit 0
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 1 << A0Mux
	pinMask |= 0 << A1Mux
	pinMask |= 0 << A0
	pinMask |= 0 << A1
	pinMask |= 0 << A2
	setGPIO(pinMask)

	time.sleep(1)

	# #001 - Encoder 2, Bit 1
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 1 << A0Mux
	pinMask |= 0 << A1Mux
	pinMask |= 1 << A0
	pinMask |= 0 << A1
	pinMask |= 0 << A2
	setGPIO(pinMask)

	time.sleep(1)

	#010 - Encoder 2, Bit 2
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 1 << A0Mux
	pinMask |= 0 << A1Mux
	pinMask |= 0 << A0
	pinMask |= 1 << A1
	pinMask |= 0 << A2
	setGPIO(pinMask)


	time.sleep(1)

	#011 - Encoder 2, Bit 3
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 1 << A0Mux
	pinMask |= 0 << A1Mux
	pinMask |= 1 << A0
	pinMask |= 1 << A1
	pinMask |= 0 << A2
	setGPIO(pinMask)

	time.sleep(1)
	clearAllGPIO()

def toggleEncoder3():
	print("Encoder #3")
	# #100 - Encoder 3, Bit 0
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 1 << A0Mux
	pinMask |= 0 << A1Mux
	pinMask |= 0 << A0
	pinMask |= 0 << A1
	pinMask |= 1 << A2
	setGPIO(pinMask)

	time.sleep(1)

	#101 - Encoder 3, Bit 1
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 1 << A0Mux
	pinMask |= 0 << A1Mux
	pinMask |= 1 << A0
	pinMask |= 0 << A1
	pinMask |= 1 << A2
	setGPIO(pinMask)

	time.sleep(1)

	#110 - Encoder 3, Bit 2
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 1 << A0Mux
	pinMask |= 0 << A1Mux
	pinMask |= 0 << A0
	pinMask |= 1 << A1
	pinMask |= 1 << A2
	setGPIO(pinMask)

	time.sleep(1)

	#111 - Encoder 3, Bit 3
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 1 << A0Mux
	pinMask |= 0 << A1Mux
	pinMask |= 1 << A0
	pinMask |= 1 << A1
	pinMask |= 1 << A2
	setGPIO(pinMask)

	time.sleep(1)
	clearAllGPIO()

def toggleEncoder4():
	print("Encoder #4")
	# # 000 - Encoder 4 - Bit 0
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 0 << A0Mux
	pinMask |= 1 << A1Mux
	pinMask |= 0 << A0
	pinMask |= 0 << A1
	pinMask |= 0 << A2
	setGPIO(pinMask)

	time.sleep(1)

	#001 - Encoder 4, Bit 1
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 0 << A0Mux
	pinMask |= 1 << A1Mux
	pinMask |= 1 << A0
	pinMask |= 0 << A1
	pinMask |= 0 << A2
	setGPIO(pinMask)

	time.sleep(1)

	#010 - Encoder 4, Bit 2
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 0 << A0Mux
	pinMask |= 1 << A1Mux
	pinMask |= 0 << A0
	pinMask |= 1 << A1
	pinMask |= 0 << A2
	setGPIO(pinMask)


	time.sleep(1)

	#011 - Encoder 4, Bit 3
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 0 << A0Mux
	pinMask |= 1 << A1Mux
	pinMask |= 1 << A0
	pinMask |= 1 << A1
	pinMask |= 0 << A2
	setGPIO(pinMask)

	time.sleep(1)
	clearAllGPIO()

def toggleEncoder5():
	print("Encoder #5")
	# #100 - Encoder 5, Bit 0
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 0 << A0Mux
	pinMask |= 1 << A1Mux
	pinMask |= 0 << A0
	pinMask |= 0 << A1
	pinMask |= 1 << A2
	setGPIO(pinMask)

	time.sleep(1)

	#101 - Encoder 5, Bit 1
	pinMask = 0
	pinMask |= 1 << muxEnable
	pinMask |= 0 << A0Mux
	pinMask |= 1 << A1Mux
	pinMask |= 1 << A0
	pinMask |= 0 << A1
	pinMask |= 1 << A2
	setGPIO(pinMask)

	time.sleep(1)

	clearAllGPIO()

# start a test
configureGPIO()
# powerButtonPress()

# leftToeButtonsPress()
# rightToeButtonsPress()
# powerMosfetOn()
# time.sleep(20)
# powerMosfetOff()
# toggleEncoder0()
toggleEncoder1()
# toggleEncoder2()
# toggleEncoder3()
# toggleEncoder4()
# toggleEncoder5()