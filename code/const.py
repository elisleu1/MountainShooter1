# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = 255, 255, 50

# E
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 5,
    'Player2': 5,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')
# P
P_MOVE_UP = {'Player1': pygame.K_w,
            'Player2': pygame.K_UP}
P_MOVE_DOWN = {'Player1': pygame.K_s,
            'Player2': pygame.K_DOWN,}
P_MOVE_LEFT = {'Player1': pygame.K_a,
            'Player2': pygame.K_LEFT}
P_MOVE_RIGHT = {'Player1': pygame.K_d,
            'Player2': pygame.K_RIGHT}
P_SHOOT = {'Player1': pygame.K_SPACE,
            'Player2': pygame.K_p}
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

