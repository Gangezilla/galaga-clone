import pygame
import os
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image('player-ship.jpeg', -1)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.size = self.image.get_size()
        self.speed = 10
        self.reinit()

    def reinit(self): # on getting hit
        self.movepos = [0,0]

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data', name)
        image = pygame.image.load(fullname)
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def move_left(self):
        self.movepos[0] = self.movepos[0] - (self.speed)

    def move_right(self):
        self.movepos[0] = self.movepos[0] + (self.speed)

    def move_up(self):
        self.movepos[1] = self.movepos[1] - (self.speed)
    
    def move_down(self):
        self.movepos[1] = self.movepos[1] + (self.speed)

    def shoot(self):
        print('pew pew')

    def update(self, dt):
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        pygame.event.pump()
