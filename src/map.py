from pygame import Surface, Vector2, Rect
from pytmx import load_pygame, TiledTileLayer
from src.camera import Camera
from src.player import Player
import settings
import math
from typing import NamedTuple
import collections


class MapOffset(NamedTuple):
    xmin: int
    xmax: int
    ymin: int
    ymax: int


class Map:

    def __init__(self, levelname: str):
        #self.player: Player = Player(position=Vector2(10, 10), velocity=Vector2(10, 10))
        self.map_object = load_pygame(levelname)
        self.map_width = self.map_object.tilewidth * self.map_object.width
        self.map_height = self.map_object.tileheight * self.map_object.height
        self.layers = []
        self.tile_width_count: int = math.ceil(settings.SCREEN_WIDTH / self.map_object.tilewidth)
        self.tile_height_count: int = math.ceil(settings.SCREEN_HEIGHT / self.map_object.tileheight)
        self.tile_height: int = int(self.map_height / self.map_object.tileheight)
        self.textures = dict()

    def __del__(self):
        pass

    def flip_y(self, ycord: int) -> int:
        return self.tile_height - ycord
