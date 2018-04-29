from player import Player

import pygame
from pygame.locals import *

class Application:
    def __init__(self):
        pygame.init()

        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Galaga Clone by an amateur')
        pygame.mouse.set_visible(0)

        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((255, 255, 255))

        screen.blit(background, (0,0))
        pygame.display.flip()

        clock = pygame.time.Clock()
        player = Player()
        playersprite = pygame.sprite.RenderPlain((player))

        going = True
        while going:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    going = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        going = False
                    if event.key == pygame.K_LEFT:
                        player.move_left()
                    if event.key == pygame.K_RIGHT:
                        player.move_right()
                    if event.key == pygame.K_UP:
                        player.move_up()
                    if event.key == pygame.K_DOWN:
                        player.move_down()
                elif event.type == pygame.KEYUP:
                    if   event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player.movepos = [0,0]
                
                
            playersprite.update()

            screen.blit(background, (0,0))
            playersprite.draw(screen)
            pygame.display.flip()

        pygame.quit()
