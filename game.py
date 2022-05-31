import pygame
from sys import exit

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

pygame.init()

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Py_Exterminator')
pygame.display.set_icon(pygame.image.load('./assets/images/icon.png'))
background = pygame.image.load('./assets/images/background_1.png')

running = True
while running:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                exit()

            elif event.type == QUIT:
                running = False
                exit()

    screen.blit(background, (0, 0))

    turret = pygame.image.load('./assets/images/turret_open.png')
    screen.blit(turret, (600, 640))

    pygame.display.flip()

pygame.quit()
