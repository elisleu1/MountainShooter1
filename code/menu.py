#!/usr/bin/python
# -*- coding: utf-8 -*-
from pydoc_data.topics import topics

import pygame.image


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')  # Load image for background
        self.rect = self.surf.get_rect(left=0, top=0)  # Create rectangle for image background

    def run(self, ):
        self.window.blit(source=self.surf, dest=self.rect)  # receive and draw image on screen
        pygame.display.flip()  # show image on screen
