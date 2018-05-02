import pygame
from pygame.locals import *

ENEMY_IMG = pygame.Surface((50, 30))
ENEMY_IMG.fill(pygame.Color('darkorange1'))

class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)
        self.image = ENEMY_IMG
        self.rect = self.image.get_rect(center=pos)
        self.health = 30

    def update(self, dt):
        if self.health <= 0:
            self.kill()