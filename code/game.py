#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import OptionMenu

import pygame

from code.menu import Menu
from code.const import *
from code.level import Level


class Game:
    def __init__(self):
        pygame.init()  # Starts pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # Create window run

    def run(self):
        # Check for all events
        while True:  # Loop that's maintain window run
            menu = Menu(self.window)  # Connecting class menu
            menu_return = menu.run()
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()

