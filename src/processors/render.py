from src import esper
from src.components.sprite import Sprite
import pygame


class RenderProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self, screen: pygame.Surface, *args, **kwargs):
        for thing in self.world.get_component(Sprite):
            # Render Everybody who has the Sprite Component
            (entity, component) = thing
            screen.blit(component.sprite, 0, 0)
