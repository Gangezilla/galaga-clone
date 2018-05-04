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
        self.shuffle_speed = 3
        self.shuffle_pos = 0
        self.shuffle_direction = 'right'

    def update(self, dt):
        if self.health <= 0:
            self.kill()

    def shuffle(self):
        if  self.shuffle_direction == 'right':
            self.rect.x += self.shuffle_speed
            self.shuffle_pos += 1
        if self.shuffle_pos == 5:
            self.shuffle_direction = 'left'
        if self.shuffle_direction == 'left':
            self.rect.x -= self.shuffle_speed
            self.shuffle_pos -= 1
        if self.shuffle_pos == -5:
            self.shuffle_direction = 'right'
            