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
        self.player: Player = Player(position=Vector2(10, 10), velocity=Vector2(10, 10))
        self.map_object = load_pygame(levelname)
        self.map_width = self.map_object.tilewidth * self.map_object.width
        self.map_height = self.map_object.tileheight * self.map_object.height
        self.layers = []
        self.tile_width_count: int = math.ceil(settings.SCREEN_WIDTH / self.map_object.tilewidth)
        self.tile_height_count: int = math.ceil(settings.SCREEN_HEIGHT / self.map_object.tileheight)
        self.tile_height: int = int(self.map_height / self.map_object.tileheight)
        self.textures = dict()
        self.preload_textures()

    def __del__(self):
        pass

    def preload_textures(self):
        for layer in self.map_object.visible_layers:
            if isinstance(layer, TiledTileLayer):
                for y in range(0, self.map_object.height):
                    for x in range(0, self.map_object.width):
                        gid = layer.data[y][x]
                        image = self.map_object.images[gid]
                        if gid not in self.textures.keys():
                            self.textures[gid] = image
                            print(repr(image))

    def flip_y(self, ycord: int) -> int:
        return self.tile_height - ycord

    def get_tile_offset(self, camera: Camera) -> NamedTuple:
        map_offsets = MapOffset
        map_offsets.xmin = math.floor(camera.camera.x / self.map_object.tilewidth)
        map_offsets.xmax = map_offsets.xmin + self.tile_width_count

        map_offsets.ymin = math.floor(camera.camera.y / self.map_object.tileheight)

        return map_offsets

    def calculate_height_in_px(self, screen_height: int, ycord: int, yoffset=0) -> int:
        return screen_height - ((self.flip_y(ycord) - yoffset) * self.map.map_object.tileheight)

    def calculate_width_in_px(self, xcord: int, xoffset=0) -> int:
        return (xcord - xoffset) * self.map_object.tilewidth
