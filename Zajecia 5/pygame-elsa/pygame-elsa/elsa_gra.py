#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame, sys
from sprites.elsa import Elsa
from sprites.anna import Anna
from sprites.wall import Wall
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 640


# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Elsa i Anna')

WHITE = (255, 255, 255)

all_sprites_list = pygame.sprite.Group()

walls = [Wall(300,i*100) for i in range(4)]

for wall in walls:
    all_sprites_list.add(wall)

elsa = Elsa(0,0, WINDOW_WIDTH, WINDOW_HEIGHT, walls)
all_sprites_list.add(elsa)
anna = Anna(800,100, WINDOW_WIDTH, WINDOW_HEIGHT)
all_sprites_list.add(anna)


background_image = pygame.image.load("images/background.png")
gameover_image = pygame.image.load("images/gameover.png")

gameover = False

pygame.mixer.init()
pygame.mixer.music.load('sounds/over.mp3')


while True: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                elsa.move_right()
            elif event.key == K_LEFT:
                elsa.move_left()
            elif event.key == K_DOWN:
                elsa.move_down()
            elif event.key == K_UP:
                elsa.move_up()
            elif event.key == K_r:
                gameover = False
                pygame.mixer.music.stop()

    all_sprites_list.update()

    if pygame.sprite.collide_rect(elsa, anna):
        gameover = True
        pygame.mixer.music.play(-1)
        elsa.reset()

    if gameover:
        DISPLAYSURF.blit(gameover_image, (0,0))

    else:
        DISPLAYSURF.blit(background_image, (0,0))
        all_sprites_list.draw(DISPLAYSURF)

    #Refresh Screen
    pygame.display.flip()

    fpsClock.tick(FPS)
