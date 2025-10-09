#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.player import  Player
from code.const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:
    @staticmethod
    def get_entity(name: str, position = (0, 0)):
        match name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH,0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 -30 ))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
        return None