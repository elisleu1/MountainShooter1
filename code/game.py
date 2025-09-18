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

        # Check for all events
        while True:  # Loop that's maintain window run
            menu = Menu(self.window)  # Connecting class menu
            menu.run()
