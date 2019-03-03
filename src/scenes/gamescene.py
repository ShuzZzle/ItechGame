import pygame

from src.scenemanager import SceneManager
from src.map import Map
from src.camera import Camera
import pytmx
import settings
import sys
from src.map import MapOffset


class GameScene(SceneManager):

    def __init__(self, levelname: str):
        super().__init__()
        self.map: Map = Map(settings.BASE_DIR + "\\" + levelname)
        self.camera: Camera = Camera(pos=pygame.Vector2(0, 0))

    def render(self, screen: pygame.Surface):
        map_offsets: MapOffset = self.map.get_tile_offset(self.camera)
        for index, layer in enumerate(self.map.map_object.visible_layers):
            for y in reversed(range(self.map.tile_height - self.map.tile_height_count, self.map.tile_height)):
                for x in range(map_offsets.xmin, map_offsets.xmax):
                    print(map_offsets.xmin, map_offsets.xmax)
                    if isinstance(layer, pytmx.TiledTileLayer):
                        tile = self.map.map_object.get_tile_image(x, y, index)
                        if tile:
                            height = screen.get_height() - (self.map.flip_y(y) * self.map.map_object.tileheight)
                            screen.blit(tile, (self.map.calculate_width_in_px(x, map_offsets.xmin), height))

    def handle_events(self, events: [pygame.event.EventType]):
        for event in events:
            if event.type == pygame.QUIT:
                self.scene = None

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT]:
            self.camera.camera.x -= 3
        if keys_pressed[pygame.K_RIGHT]:
            self.camera.camera.x += 3

    def update(self, delta=1):
        pass

