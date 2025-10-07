#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame.font import Font
from pygame import Surface, Rect
from code.const import *


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')  # Load image for background
        self.rect = self.surf.get_rect(left=0, top=0)  # Create rectangle for image background

    def run(self, ):
        menu_op = 0
        # Menu Music
        pygame.mixer_music.load('./asset/Menu.mp3')  # Load music
        pygame.mixer_music.play(-1)  # Play a music loaded     # the parameter '(-1)' plays the sound in loop.
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # receive and draw image on screen

            # Show title menu (text)
            self.menu_text(50, 'Mountain', COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, 'Shooter', COLOR_ORANGE, ((WIN_WIDTH / 2), 120))
            # Show options menu (text)
            for i in range(len(MENU_OPTION)):
                if i == menu_op:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()  # show image on screen# Create Text Title Menu
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # Key Down Arow
                        if menu_op < len(MENU_OPTION) -1:
                            menu_op += 1
                        else:
                            menu_op = 0
                    if event.key == pygame.K_UP:    # Key Up Arow
                        if menu_op > 0:
                            menu_op -= 1
                        else:
                            menu_op = len(MENU_OPTION) -1

                    if event.key == pygame.K_RETURN:    # Return Key Op to  Level
                        return MENU_OPTION[menu_op]

    # Create text like image
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucia Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
