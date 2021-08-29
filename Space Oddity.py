import time
import emoji
import pygame
print('-'*150)
print('\033[0;32mGROUND CONTROL: Seja bem-vindo à decolagem do Major Tom!\033[m')
print('')
time.sleep(3)
pygame.mixer.init()
pygame.mixer.music.load('C:/Users/usuario/Desktop/decolagem.mp3')
pygame.mixer.music.play(999)
x = 20
for a in range(10, 0, -1):
    time.sleep(1)
    print(' '*x, a)
    x -= 2
print('')
print(emoji.emojize(':rocket:', use_aliases=True))
print('')
time.sleep(1)
print('THIS IS GROUND CONTROL TO MAJOR TOM')
time.sleep(5)
print('YOU REALLY MADE THE GRADE')
time.sleep(5)
print('AND THE PAPERS WANT TO KNOW WHOSE SHIRTS YOU WEAR')
time.sleep(7)
print('NOW ITS TIME TO LEAVE THE CAPSULE IF YOU DARE')
time.sleep(7.5)
print('THIS IS MAJOR TOM TO GROUND CONTROL')
time.sleep(5)
print('IM STEPPING THROUGH THE DOOR')
time.sleep(3.5)
print('...')