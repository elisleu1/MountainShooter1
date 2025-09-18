#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import Menu


class Game:
    def __init__(self):
        self.window = None

    def run(self, ):
        pygame.init()  # Starts pygame
        window = pygame.display.set_mode(size=(600, 480))  # Create window run

        while True:  # Loop that's maintain window run
            menu = Menu(self.window)    # Connecting class menu
            menu.run()
            # Check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()  # Close window
            #         quit()  # End pygame
            # pass
