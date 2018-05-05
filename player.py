import pygame
import os
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image('player-ship.jpeg', -1)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=(pos))
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.size = self.image.get_size()
        self.speed = 10
        self.health = 10
        self.invulnerability_timer = 300
        self.is_dead = False
        self.is_invulnerable = False

    # def reinit(self): # on getting hit
    #     self.movepos = [0,0]

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
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

    def move_up(self):
        self.rect.y -= self.speed
    
    def move_down(self):
        self.rect.y += self.speed

    def get_pos(self):
        return (self.rect.x, self.rect.y)

    def take_hit(self, damage):
        if self.health > 0:
            self.health -= damage
        else:
            self.is_dead = True


    def update(self, dt):
        if self.health <= 0 and not self.is_invulnerable:
            self.kill()
        if self.is_dead:
            self.is_invulnerable = True

        if self.is_invulnerable and self.invulnerability_timer > 0:
            print('!33333', self.invulnerability_timer, self.is_invulnerable)
            self.invulnerability_timer -= 1
        elif self.invulnerability_timer <= 0:
            print('!!', self.invulnerability_timer, self.is_invulnerable)
            self.is_invulnerable = False
            self.invulnerability_timer = 300

