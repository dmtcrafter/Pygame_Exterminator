import pygame
from sys import exit

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
        if event.type == pygame.QUIT:
            running = False
            exit()

    screen.blit(background, (0, 0))

    pygame.draw.circle(screen, (0, 255, 255), (500, 400), 75)

    pygame.display.flip()

pygame.quit()
