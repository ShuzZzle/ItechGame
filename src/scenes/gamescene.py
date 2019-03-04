import pygame

from src.scenemanager import SceneManager
from src.map import Map
from src.camera import Camera
import pytmx
import settings
from src.util import clamp


class GameScene(SceneManager):

    def __init__(self, levelname: str):
        super().__init__()
        self.map: Map = Map(settings.BASE_DIR + "\\" + levelname)
        self.camera: Camera = Camera()

    def render(self, screen: pygame.Surface):
        for index, layer in enumerate(self.map.map_object.visible_layers):
            for y in reversed(range(0, self.map.map_object.height)):
                for x in range(0, self.map.map_object.width):
                    if isinstance(layer, pytmx.TiledTileLayer):
                        tile = self.map.map_object.get_tile_image(x, y, index)
                        if tile:
                            height = screen.get_height() - (self.map.flip_y(y) * self.map.map_object.tileheight)
                            position = (x * self.map.map_object.tilewidth) - self.camera.camera.x
                            screen.blit(tile, (position, height))

    def handle_events(self, events: [pygame.event.EventType]):
        for event in events:
            if event.type == pygame.QUIT:
                self.scene = None

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT]:
            self.camera.camera.x = clamp(self.camera.camera.x-10, 0, (self.map.map_width - settings.SCREEN_WIDTH))
        if keys_pressed[pygame.K_RIGHT]:
            self.camera.camera.x = clamp(self.camera.camera.x+10, 0, (self.map.map_width - settings.SCREEN_WIDTH))

    def update(self, delta=1):
        pass

