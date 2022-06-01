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


class Player(pygame.sprite.Sprite):

    surf = pygame.image.load('./assets/images/player_bot_1.png')
    rect = surf.get_rect()
    rect.center = (200, 640)
    gravity = 0

    def __init__(self):
        super(Player, self).__init__()

    def update(self):

        if Player.rect.bottomy >= 640:
            Player.rect.bottomy = 640

        if Player.rect.right >= 1200:
            Player.rect.right = 1200

        if Player.rect.left >= 0:
            Player.rect.left = 0


sprites = pygame.sprite.Group()

player = Player()
sprites.add(player)

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

    player.gravity += 1

    player.rect.move_ip(0, player.gravity)

    screen.blit(background, (0, 0))

    screen.blit(Player.surf, Player.rect.center)

    pygame.display.flip()

pygame.quit()
