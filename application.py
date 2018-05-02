from player import Player
from bullet import Bullet
from enemy import Enemy
import random

import pygame
from pygame.locals import *

class Application:
    def __init__(self):
        self.going = True
        pygame.init()
        print('init')
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.color_bg = pygame.Color("gray")

        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()

        player_pos = (100, 100)
        self.player = Player(player_pos, self.all_sprites, self.player_sprite)
        self.bullets = pygame.sprite.Group()
        self.bullet_timer = .1

        for i in range(15):
            pos = (random.randrange(30, 750), random.randrange(500))
            Enemy(pos, self.all_sprites, self.enemies)

    def run(self):
        print('run')
        while self.going:
            dt = self.clock.tick(60) / 1000
            self.handle_events()
            self.run_logic(dt)
            self.draw()

    def draw(self):
        self.screen.fill(self.color_bg)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def run_logic(self, dt):
        self.all_sprites.update(dt)
        self.bullet_timer -= dt
        # if self.bullet_timer <= 0:
        # hits = pg.sprite.groupcollide(self.enemies, self.bullets, False, True)
        # for enemy, bullet_list in hits.items():
        #     for bullet in bullet_list:
        #         enemy.health -= bullet.damage


    def handle_events(self):
        for event in pygame.event.get():
            keys = pygame.key.get_pressed() # keys shows you what is being pressed when it gets called.
            if event.type == pygame.QUIT:
                self.going = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: self.going = False
                if event.key == pygame.K_LEFT: self.player.move_left()
                if event.key == pygame.K_RIGHT: self.player.move_right()
                if event.key == pygame.K_UP: self.player.move_up()
                if event.key == pygame.K_DOWN: self.player.move_down()
                if keys[K_SPACE]: self.player.shoot()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.player.movepos = [0,0]
