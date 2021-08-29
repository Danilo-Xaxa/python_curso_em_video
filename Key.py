import time
import emoji
import pygame
print('-'*150)
time.sleep(3)
print('\033[1;35mTU É KEY\033[m')
pygame.mixer.init()
pygame.mixer.music.load('C:/Users/usuario/Desktop/decolagem.mp3')
pygame.mixer.music.play(999)
print('')
print(emoji.emojize(':key:', use_aliases=True))