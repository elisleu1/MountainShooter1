#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.const import WIN_HEIGHT, COLOR_WHITE
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)


            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest= ent.rect)
                ent.move()
                self.level_text(20, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}', COLOR_WHITE, (10, 20))
                self.level_text(20, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, 300))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucia Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
