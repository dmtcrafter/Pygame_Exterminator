from utils import*
from sys import exit

from pygame.locals import (
    K_ESCAPE,
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

sprites = pygame.sprite.Group()

pressed_keys = pygame.key.get_pressed()

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

    screen.blit(background, (0, 0))

    screen.blit(Player.surf, Player.rect.center)

    pygame.display.flip()

pygame.quit()
