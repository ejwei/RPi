# Import standard Python time library.
import time

# Import GPIO and FT232H modules.
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.FT232H as FT232H



#Pin Definitions
A0Mux = 8
A1Mux = 5
muxEnable = 3

A0 = 9
A1 = 10
A2 = 11

LED = 4




def muxSetup():
	# Configure digital inputs and outputs using the setup function.
	# Note that pin numbers 0 to 15 map to pins D0 to D7 then C0 to C7 on the board.
	ft232h.setup(A0Mux, GPIO.OUT)
	ft232h.setup(A1Mux, GPIO.OUT)
	ft232h.setup(muxEnable, GPIO.OUT)

	ft232h.setup(A0, GPIO.OUT)
	ft232h.setup(A1, GPIO.OUT)
	ft232h.setup(A2, GPIO.OUT)

def powerButtonPress():
	ft232h.output(muxEnable, GPIO.HIGH)
	#100 - Power Button
	ft232h.output(A0Mux, GPIO.HIGH)
	ft232h.output(A1Mux, GPIO.HIGH)
	ft232h.output(A0,GPIO.LOW)
	ft232h.output(A1,GPIO.LOW)
	ft232h.output(A2,GPIO.HIGH)

	time.sleep(1)

	ft232h.output(muxEnable, GPIO.LOW)
	ft232h.output(A0Mux, GPIO.LOW)
	ft232h.output(A1Mux, GPIO.LOW)
	ft232h.output(A0,GPIO.LOW)
	ft232h.output(A1,GPIO.LOW)
	ft232h.output(A2,GPIO.LOW)



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


# Temporarily disable the built-in FTDI serial driver on Mac & Linux platforms.
FT232H.use_FT232H()

# Create an FT232H object that grabs the first available FT232H device found.
ft232h = FT232H.FT232H()
print 'Press Ctrl-C to quit.'

muxSetup()
# toggleEncoder0()
# toggleEncoder1()
toggleEncoder2()
toggleEncoder3()
# toggleEncoder4()
# toggleEncoder5()