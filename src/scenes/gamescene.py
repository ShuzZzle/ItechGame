import pygame

from src.scenemanager import SceneManager


class GameScene(SceneManager):

    def __init__(self):
        SceneManager.__init__(self)

    def render(self):
        pass

    def handle_events(self, events: [pygame.event.EventType]):
        for event in events:
            if event.type == pygame.QUIT:
                self.scene = None

    def update(self, delta=1):
        pass

