#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *

class Anna(pygame.sprite.Sprite):
    def __init__(self, x, y, window_width, window_height):
        pygame.sprite.Sprite.__init__(self)

        self.window_width = window_width
        self.window_height = window_height

        # Set height, width
        self.image = pygame.image.load("images/anna.png")

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
