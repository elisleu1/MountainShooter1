#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import Menu
from .const import *


class Game:
    def __init__(self):
        self.window = None

    def run(self, ):
        pygame.init()  # Starts pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # Create window run
        # Menu Music
        pygame.mixer_music.load('./asset/Menu.mp3')  # Load music
        pygame.mixer_music.play(-1)  # Play a music loaded     # the parameter '(-1)' plays the sound in loop.

        # Check for all events
        while True:  # Loop that's maintain window run
            menu = Menu(self.window)  # Connecting class menu
            menu.run()
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame
