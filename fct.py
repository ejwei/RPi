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

	# ft232h.output(A0Mux, GPIO.LOW)
	# ft232h.output(A1Mux, GPIO.HIGH)
	# ft232h.output(A0,GPIO.LOW)
	# ft232h.output(A1,GPIO.HIGH)
	# ft232h.output(A2,GPIO.HIGH)

	time.sleep(1)

	#111 - Right Leg 1
	print("[FCT TESTER] R1 Button")
	# ft232h.output(A0Mux, GPIO.LOW)
	# ft232h.output(A1Mux, GPIO.HIGH)
	# ft232h.output(A0,GPIO.HIGH)
	# ft232h.output(A1,GPIO.HIGH)
	# ft232h.output(A2,GPIO.HIGH)

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
	# ft232h.output(A0Mux, GPIO.HIGH)
	# ft232h.output(A1Mux, GPIO.HIGH)
	# ft232h.output(A0, GPIO.LOW)
	# ft232h.output(A1, GPIO.LOW)
	# ft232h.output(A2, GPIO.LOW)

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
	# ft232h.output(A0Mux, GPIO.HIGH)
	# ft232h.output(A1Mux, GPIO.HIGH)
	# ft232h.output(A0, GPIO.HIGH)
	# ft232h.output(A1, GPIO.LOW)
	# ft232h.output(A2, GPIO.LOW)

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
	# ft232h.output(A0Mux, GPIO.HIGH)
	# ft232h.output(A1Mux, GPIO.HIGH)
	# ft232h.output(A0, GPIO.LOW)
	# ft232h.output(A1, GPIO.HIGH)
	# ft232h.output(A2, GPIO.LOW)

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
	# ft232h.output(A0Mux, GPIO.HIGH)
	# ft232h.output(A1Mux, GPIO.HIGH)
	# ft232h.output(A0, GPIO.HIGH)
	# ft232h.output(A1, GPIO.HIGH)
	# ft232h.output(A2, GPIO.LOW)

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
	# ft232h.output(muxEnable, GPIO.LOW)

	# time.sleep(2)

	# ft232h.output(muxEnable, GPIO.HIGH)
	# ft232h.output(A0Mux, GPIO.HIGH)
	# ft232h.output(A1Mux, GPIO.HIGH)

	# time.sleep(1)

	# #101 (Y5)
	# ft232h.output(A0,GPIO.HIGH)
	# ft232h.output(A1,GPIO.LOW)
	# ft232h.output(A2,GPIO.HIGH)

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
	ft232h.output(muxEnable, GPIO.HIGH)
	ft232h.output(A0Mux, GPIO.LOW)
	ft232h.output(A1Mux, GPIO.LOW)

	# 000 - Encoder 0, Bit 0
	ft232h.output(A0, GPIO.LOW)
	ft232h.output(A1, GPIO.LOW)
	ft232h.output(A2, GPIO.LOW)

	time.sleep(1)

	#001 - Encoder 0, Bit 1
	ft232h.output(A0, GPIO.HIGH)
	ft232h.output(A1, GPIO.LOW)
	ft232h.output(A2, GPIO.LOW)


	time.sleep(1)

	#010 - Encoder 0, Bit 2
	ft232h.output(A0, GPIO.LOW)
	ft232h.output(A1, GPIO.HIGH)
	ft232h.output(A2, GPIO.LOW)


	time.sleep(1)

	#011 - Encoder 0, Bit 3
	ft232h.output(A0, GPIO.HIGH)
	ft232h.output(A1, GPIO.HIGH)
	ft232h.output(A2, GPIO.LOW)

	time.sleep(1)
	ft232h.output(muxEnable, GPIO.LOW)

def toggleEncoder1():
	print("Encoder #1")
	ft232h.output(muxEnable, GPIO.HIGH)
	#100 - Encoder 1, Bit 0
	ft232h.output(A0,GPIO.LOW)
	ft232h.output(A1,GPIO.LOW)
	ft232h.output(A2,GPIO.HIGH)

	time.sleep(1)

	#101 - Encoder 1, Bit 1
	ft232h.output(A0,GPIO.HIGH)
	ft232h.output(A1,GPIO.LOW)
	ft232h.output(A2,GPIO.HIGH)

	time.sleep(1)

	#110 - Encoder 1, Bit 2
	ft232h.output(A0,GPIO.LOW)
	ft232h.output(A1,GPIO.HIGH)
	ft232h.output(A2,GPIO.HIGH)

	time.sleep(1)

	#111 - Encoder 1, Bit 3
	ft232h.output(A0,GPIO.HIGH)
	ft232h.output(A1,GPIO.HIGH)
	ft232h.output(A2,GPIO.HIGH)

	time.sleep(2)
	ft232h.output(muxEnable, GPIO.LOW)


def toggleEncoder2():
	print("Encoder #2")
	ft232h.output(muxEnable, GPIO.HIGH)
	ft232h.output(A0Mux, GPIO.HIGH)
	ft232h.output(A1Mux, GPIO.LOW)
	# 000 - Encoder 2, Bit 0
	ft232h.output(A0, GPIO.LOW)
	ft232h.output(A1, GPIO.LOW)
	ft232h.output(A2, GPIO.LOW)

	time.sleep(25)

	#001 - Encoder 2, Bit 1
	ft232h.output(A0, GPIO.HIGH)
	ft232h.output(A1, GPIO.LOW)
	ft232h.output(A2, GPIO.LOW)


	time.sleep(5)

	#010 - Encoder 2, Bit 2
	ft232h.output(A0, GPIO.LOW)
	ft232h.output(A1, GPIO.HIGH)
	ft232h.output(A2, GPIO.LOW)


	time.sleep(5)

	#011 - Encoder 2, Bit 3
	ft232h.output(A0, GPIO.HIGH)
	ft232h.output(A1, GPIO.HIGH)
	ft232h.output(A2, GPIO.LOW)

	time.sleep(5)
	ft232h.output(muxEnable, GPIO.LOW)

def toggleEncoder3():
	print("Encoder #3")
	ft232h.output(muxEnable, GPIO.HIGH)
	#100 - Encoder 3, Bit 0
	ft232h.output(A0,GPIO.LOW)
	ft232h.output(A1,GPIO.LOW)
	ft232h.output(A2,GPIO.HIGH)

	time.sleep(5)

	#101 - Encoder 3, Bit 1
	ft232h.output(A0,GPIO.HIGH)
	ft232h.output(A1,GPIO.LOW)
	ft232h.output(A2,GPIO.HIGH)

	time.sleep(5)

	#110 - Encoder 3, Bit 2
	ft232h.output(A0,GPIO.LOW)
	ft232h.output(A1,GPIO.HIGH)
	ft232h.output(A2,GPIO.HIGH)

	time.sleep(5)

	#111 - Encoder 3, Bit 3
	ft232h.output(A0,GPIO.HIGH)
	ft232h.output(A1,GPIO.HIGH)
	ft232h.output(A2,GPIO.HIGH)

	time.sleep(2)
	ft232h.output(muxEnable, GPIO.LOW)

def toggleEncoder4():
	print("Encoder #4")
	ft232h.output(muxEnable, GPIO.HIGH)
	ft232h.output(A0Mux, GPIO.LOW)
	ft232h.output(A1Mux, GPIO.HIGH)

	# 000 - Encoder 4 - Bit 0
	ft232h.output(A0, GPIO.LOW)
	ft232h.output(A1, GPIO.LOW)
	ft232h.output(A2, GPIO.LOW)

	time.sleep(1)

	#001 - Encoder 4, Bit 1
	ft232h.output(A0, GPIO.HIGH)
	ft232h.output(A1, GPIO.LOW)
	ft232h.output(A2, GPIO.LOW)


	time.sleep(1)

	#010 - Encoder 4, Bit 2
	ft232h.output(A0, GPIO.LOW)
	ft232h.output(A1, GPIO.HIGH)
	ft232h.output(A2, GPIO.LOW)


	time.sleep(1)

	#011 - Encoder 4, Bit 3
	ft232h.output(A0, GPIO.HIGH)
	ft232h.output(A1, GPIO.HIGH)
	ft232h.output(A2, GPIO.LOW)

	time.sleep(1)
	ft232h.output(muxEnable, GPIO.LOW)


def toggleEncoder5():
	print("Encoder #5")
	ft232h.output(muxEnable, GPIO.HIGH)
	#100 - Encoder 5, Bit 0
	ft232h.output(A0,GPIO.LOW)
	ft232h.output(A1,GPIO.LOW)
	ft232h.output(A2,GPIO.HIGH)

	time.sleep(1)

	#101 - Encoder 5, Bit 1
	ft232h.output(A0,GPIO.HIGH)
	ft232h.output(A1,GPIO.LOW)
	ft232h.output(A2,GPIO.HIGH)

	time.sleep(1)

	ft232h.output(muxEnable, GPIO.LOW)

configureGPIO()
# powerButtonPress()

# leftToeButtonsPress()
# rightToeButtonsPress()
powerMosfetOn()
time.sleep(20)
powerMosfetOff()