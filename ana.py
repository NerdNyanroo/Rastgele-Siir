import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import sys
import os
import time
import subprocess

exec(open("reset.py").read())

GPIO.setwarnings(True) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

while True: # Run forever
    if GPIO.input(8) == GPIO.HIGH:
        exec(open("tanzimat.py").read())
    if GPIO.input(10) == GPIO.HIGH:
        exec(open("tanzimat2.py").read())
    if GPIO.input(12) == GPIO.HIGH:
        exec(open("servetifunun.py").read())
    if GPIO.input(16) == GPIO.HIGH:
        exec(open("fecriati.py").read())
    if GPIO.input(18) == GPIO.HIGH:
        exec(open("bagımsız.py").read())
    if GPIO.input(22) == GPIO.HIGH:
        exec(open("milli.py").read())
        
GPIO.cleanup()
