import pygame
import random
import os
import sys
import subprocess

pygame.init()
display=pygame.display.set_mode((400,300))
pygame.display.set_caption("servetifunun")
servetifunun=[".mp3",".mp3",".mp3"]
pygame.mixer.music.load(random.choice(servetifunun))
pygame.mixer.music.play()
while True:
      for eve in pygame.event.get():
            if eve.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
