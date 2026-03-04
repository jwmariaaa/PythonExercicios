import pygame
import time
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Sweater Weather - The Neighbourhood (youtube).mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(1)

