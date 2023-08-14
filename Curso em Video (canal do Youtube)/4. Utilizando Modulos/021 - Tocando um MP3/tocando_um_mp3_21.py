"""
Programa que executa e reproduz o áudio de um arquivo mp3.
"""

import pygame

pygame.init()
pygame.mixer.music.load('C:\house_lo.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass
