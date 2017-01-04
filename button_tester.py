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
	ft232h.setup(A0Mux, GPIO.OUT)
	ft232h.setup(A1Mux, GPIO.OUT)
	ft232h.setup(muxEnable, GPIO.OUT)

	ft232h.setup(A0, GPIO.OUT)
	ft232h.setup(A1, GPIO.OUT)
	ft232h.setup(A2, GPIO.OUT)


def rightToeButtonsPress():
	ft232h.output(muxEnable, GPIO.HIGH)
	#110 - Right Leg 0
	time.sleep(1)

	print("[FCT TESTER] R0 Button")
	ft232h.output(A0Mux, GPIO.LOW)
	ft232h.output(A1Mux, GPIO.HIGH)
	ft232h.output(A0,GPIO.LOW)
	ft232h.output(A1,GPIO.HIGH)
	ft232h.output(A2,GPIO.HIGH)

	time.sleep(1)

	#111 - Right Leg 1
	print("[FCT TESTER] R1 Button")
	ft232h.output(A0Mux, GPIO.LOW)
	ft232h.output(A1Mux, GPIO.HIGH)
	ft232h.output(A0,GPIO.HIGH)
	ft232h.output(A1,GPIO.HIGH)
	ft232h.output(A2,GPIO.HIGH)
	
	time.sleep(1)

	# 000 - Right Leg 2
	print("[FCT TESTER] R2 Button")
	ft232h.output(A0Mux, GPIO.HIGH)
	ft232h.output(A1Mux, GPIO.HIGH)
	ft232h.output(A0, GPIO.LOW)
	ft232h.output(A1, GPIO.LOW)
	ft232h.output(A2, GPIO.LOW)

	time.sleep(1)

	ft232h.output(muxEnable, GPIO.LOW)

def leftToeButtonsPress():
	ft232h.output(muxEnable, GPIO.HIGH)
	#001 - Left Leg 0

	time.sleep(1)
	print("[FCT TESTER] L0 Button")
	ft232h.output(A0Mux, GPIO.HIGH)
	ft232h.output(A1Mux, GPIO.HIGH)
	ft232h.output(A0, GPIO.HIGH)
	ft232h.output(A1, GPIO.LOW)
	ft232h.output(A2, GPIO.LOW)


	time.sleep(1)

	#010 - Left Leg 1
	print("[FCT TESTER] L1 Button")
	ft232h.output(A0Mux, GPIO.HIGH)
	ft232h.output(A1Mux, GPIO.HIGH)
	ft232h.output(A0, GPIO.LOW)
	ft232h.output(A1, GPIO.HIGH)
	ft232h.output(A2, GPIO.LOW)


	time.sleep(1)

	#011 - Left Leg 2
	print("[FCT TESTER] L2 Button")
	ft232h.output(A0Mux, GPIO.HIGH)
	ft232h.output(A1Mux, GPIO.HIGH)
	ft232h.output(A0, GPIO.HIGH)
	ft232h.output(A1, GPIO.HIGH)
	ft232h.output(A2, GPIO.LOW)

	time.sleep(1)

	ft232h.output(muxEnable, GPIO.LOW)


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




# Temporarily disable the built-in FTDI serial driver on Mac & Linux platforms.
FT232H.use_FT232H()

# Create an FT232H object that grabs the first available FT232H device found.
ft232h = FT232H.FT232H()

# Configure digital inputs and outputs using the setup function.
# Note that pin numbers 0 to 15 map to pins D0 to D7 then C0 to C7 on the board.
# ft232h.setup(7, GPIO.IN)   # Make pin D7 a digital input.
ft232h.setup(LED, GPIO.OUT)  # Make pin C0 a digital output.

# Loop turning the LED on and off and reading the input state.
print 'Press Ctrl-C to quit.'
# while True:
# Set pin C0 to a high level so the LED turns on.
ft232h.output(LED, GPIO.HIGH)
# Sleep for 1 second.
time.sleep(1)
# Set pin C0 to a low level so the LED turns off.
ft232h.output(LED, GPIO.LOW)
# Sleep for 1 second.
time.sleep(1)
# # Read the input on pin D7 and print out if it's high or low.
# level = ft232h.input(7)
# if level == GPIO.LOW:
# 	print 'Pin D7 is LOW!'
# else:
# 	print 'Pin D7 is HIGH!'
muxSetup()
powerButtonPress()
# leftToeButtonsPress()
# rightToeButtonsPress()