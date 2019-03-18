import pygame
from src.camera import Camera


class Entity:

    def __init__(self, position: pygame.Vector2, velocity: pygame.Vector2):
        self.position = position
        self.velocity = velocity

    def update(self, delta=1):
        raise NotImplementedError

    def render(self, screen: pygame.Surface):
        raise NotImplementedError

    def handle_events(self, events: [pygame.event.EventType]):
        raise NotImplementedError
