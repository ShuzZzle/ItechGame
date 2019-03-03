import pygame
import settings


class SceneManager:

    def __init__(self):
        self.scene = self

    def update(self, delta=1):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    def handle_events(self):
        raise NotImplementedError

    def change_scene(self, scene):
        """
        Changes the current scene to the next scene.
        Args:
            scene: The next Scene to be displayed

        Returns:

        """
        self.scene = scene

    def exit(self):
        self.change_scene(None)
