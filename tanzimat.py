import pygame
import random
import os
import sys
import time
import subprocess
import RPi.GPIO as GPIO

exec(open("reset.py").read())

GPIO.setwarnings(True) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)


tanzimat=["tekribibend.mp3","ArziMuhabbet.mp3","vatansarkisi.mp3"]
x = random.choice(tanzimat)

if x == ("tekribibend.mp3"):
    GPIO.output(5, GPIO.HIGH)
    
if x == ("vatansarkisi.mp3"):
    GPIO.output(3, GPIO.HIGH)

if x == ("ArziMuhabbet.mp3"):
    GPIO.output(7, GPIO.HIGH)

pygame.init()
display=pygame.display.set_mode((400,300))
pygame.display.set_caption("tanzimat")
pygame.mixer.music.load(x)
pygame.mixer.music.play()
while True:
      for eve in pygame.event.get():
            if eve.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()

GPIO.cleanup()
