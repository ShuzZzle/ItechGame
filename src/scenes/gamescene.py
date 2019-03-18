import pygame

from src.scenemanager import SceneManager
from src.map import Map
from src.camera import Camera
import pytmx
import settings
from src.util import clamp
from src import esper
from src.components.velocity import Velocity
from src.components.position import Position


class GameScene:

    def __init__(self, levelname: str, world: esper.World):
        super().__init__()
        self.scene = self
        self.map: Map = Map(settings.BASE_DIR + "\\" + levelname)
        self.camera: Camera = Camera()
        self.entities = []
        self.player = world.create_entity()
        self.world = world
        self.world.add_component(self.player, Velocity(0, 0))
        self.world.add_component(self.player, Position(x=5, y=5))
        self.entities.append(self.player)

    def render(self, screen: pygame.Surface):
        for index, layer in enumerate(self.map.map_object.visible_layers):
            for y in reversed(range(0, self.map.map_object.height)):
                for x in range(0, self.map.map_object.width):
                    if isinstance(layer, pytmx.TiledTileLayer):
                        tile = self.map.map_object.get_tile_image(x, y, index)
                        if tile:
                            height = screen.get_height() - (self.map.flip_y(y) * self.map.map_object.tileheight)
                            height = height - self.camera.camera.y
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
        if keys_pressed[pygame.K_UP]:
            self.camera.camera.y = clamp(self.camera.camera.y-10, -1 * (self.map.map_height - settings.SCREEN_HEIGHT), 0)
        if keys_pressed[pygame.K_DOWN]:
            self.camera.camera.y = clamp(self.camera.camera.y+10, -1 * (self.map.map_height - settings.SCREEN_HEIGHT), 0)

    def update(self, delta):
        # print(delta)
        self.world.process(delta)

