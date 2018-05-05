import pygame
import os
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):

  def __init__(self, pos, isEnemy, *sprite_groups):
    BULLET_IMG = pygame.Surface((9, 15))
    super().__init__(*sprite_groups)
    self.image = BULLET_IMG
    self.rect = self.image.get_rect(center=pos)
    self.pos = pygame.math.Vector2(pos)
    if isEnemy:
      self.vel = pygame.math.Vector2(0, 450)
      BULLET_IMG.fill(pygame.Color('red'))
    else:
      self.vel = pygame.math.Vector2(0, -450)
      BULLET_IMG.fill(pygame.Color('aquamarine2'))
      
    self.damage = 10

  def update(self, dt):
    self.pos += self.vel * dt
    self.rect.center = self.pos
    if self.rect.bottom <= 0:
      self.kill()