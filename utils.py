import pygame


from pygame.locals import (

    K_LEFT,
    K_RIGHT,
    K_SPACE,
)

pressed_keys = pygame.key.get_pressed()


class Player(pygame.sprite.Sprite):

    surf = pygame.image.load('./assets/images/player_bot_1.png')
    rect = surf.get_rect()
    rect.center = (200, 640)
    gravity = 0

    def __init__(self):
        super(Player, self).__init__()

    def update(self):

        if self.rect.bottomy >= 640:
            self.rect.bottomy = 640

        if self.rect.right >= 1200:
            self.rect.right = 1200

        if self.rect.left >= 0:
            self.rect.left = 0

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(1, 0)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(-1, 0)

        self.gravity += 1

        self.rect.move_ip(0, self.gravity)
