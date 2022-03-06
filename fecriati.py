import pygame
import random
import os
import sys
import subprocess

pygame.init()
display=pygame.display.set_mode((400,300))
pygame.display.set_caption("fecriati")
fecriati=["hastateldehastabirnagme.mp3","gurbetgeceleri.mp3","merdiven.mp3"]
pygame.mixer.music.load(random.choice(fecriati))
pygame.mixer.music.play()
while True:
      for eve in pygame.event.get():
            if eve.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
