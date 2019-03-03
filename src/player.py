import pygame

from src.entity import Entity


class Player(Entity):

    def __init__(self, position: pygame.Vector2, velocity: pygame.Vector2):
        super().__init__(position, velocity)

    def update(self, delta=1):
        pass

    def handle_events(self, events: [pygame.event.EventType]):
        pass
