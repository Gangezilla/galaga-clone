from player import Player

import pygame
from pygame.locals import *

class Application:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        print('init')
        self.clock = pygame.time.Clock()
        self.going = True
        # pygame.display.set_caption('Galaga Clone by an amateur')
        # pygame.mouse.set_visible(0)

        # self.background = pygame.Surface(self.screen.get_size())
        # self.background = self.background.convert()
        # self.background.fill((0, 0, 0))

        # self.screen.blit(self.background, (0,0))
        # pygame.display.flip()

        self.player = Player()
        self.playersprite = pygame.sprite.RenderPlain((self.player))
        self.bullets = pygame.sprite.Group()
        self.bullet_timer = .1
        self.run()

    def run(self):
        print('run')
        while self.going:
            dt = self.clock.tick(60) / 1000
            self.handle_events()
            # self.run_logic(dt)
            self.draw()

    def draw(self):
        self.playersprite.update()
        # self.screen.blit(self.background, (0,0))
        self.screen.fill(0, 0, 0)
        self.playersprite.draw(self.screen)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            keys = pygame.key.get_pressed() # keys shows you what is being pressed when it gets called.
            if event.type == pygame.QUIT:
                self.going = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.going = False
                if event.key == pygame.K_LEFT:
                    self.player.move_left()
                if event.key == pygame.K_RIGHT:
                    self.player.move_right()
                if event.key == pygame.K_UP:
                    self.player.move_up()
                if event.key == pygame.K_DOWN:
                    self.player.move_down()
                if keys[K_SPACE]:
                    self.player.shoot()
            elif event.type == pygame.KEYUP:
                if   event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.player.movepos = [0,0]

        pygame.quit()
