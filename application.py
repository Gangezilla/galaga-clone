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
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.color_bg = pygame.Color("gray")

        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()

        player_pos = (400, 500)
        self.player = Player(player_pos, self.all_sprites, self.player_sprite)
        self.bullets = pygame.sprite.Group()
        self.bullet_timer = .1
        
        self.enemyObjects = []

        enemy_positions = [
            (108, 30),
            (246, 30),
            (384, 30),
            (522, 30),
            (660, 30),
            (54, 90),
            (192, 90),
            (330, 90),
            (468, 90),
            (606, 90),
            (744, 90),
            (108, 150),
            (246, 150),
            (384, 150),
            (522, 150),
            (660, 150),
        ]

        for enemy in range(len(enemy_positions)):
            pos = enemy_positions[enemy]
            enemyObj = Enemy(pos, self.all_sprites, self.enemies)
            self.enemyObjects.append(enemyObj)

    def run(self):
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
        keys = pygame.key.get_pressed()
        self.all_sprites.update(dt)
        self.bullet_timer -= dt

        if self.bullet_timer <= 0:
            self.bullet_timer = 0
            if keys[K_SPACE]:
                Bullet(self.player.get_pos(), self.all_sprites, self.bullets)
                self.bullet_timer = .1

        hits = pygame.sprite.groupcollide(self.enemies, self.bullets, False, True)
        for enemy, bullet_list in hits.items():
            for bullet in bullet_list:
                enemy.health -= bullet.damage

        for enemy in range(len(self.enemyObjects)):
            self.enemyObjects[enemy].shuffle()


    def handle_events(self):
        keys = pygame.key.get_pressed() # keys shows you what is being pressed when it gets called.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.going = False
        if keys[pygame.K_ESCAPE]: self.going = False
        if keys[pygame.K_LEFT]: self.player.move_left()
        if keys[pygame.K_RIGHT]: self.player.move_right()
        if keys[pygame.K_UP]: self.player.move_up()
        if keys[pygame.K_DOWN]: self.player.move_down()
