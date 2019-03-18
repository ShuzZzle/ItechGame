# ItechGame Constants
import pygame
import os

GAME_TITLE = "A Game"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TICKRATE = 60

SCREEN_SIZE = pygame.Rect((0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

TILE_WIDTH = 32
TILE_HEIGHT = 32

GRAVITY = pygame.Vector2()
GRAVITY.x = 0
GRAVITY.y = 0.3

LEVEL1 = "assets\\levels\\level1.tmx"

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
