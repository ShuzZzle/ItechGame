import pygame
import settings
from src.scenemanager import SceneManager
from src.scenes.gamescene import GameScene


class ItechGame:

    def __init__(self):
        self.running: bool = True
        self.tickrate: int = settings.TICKRATE
        self.delta_time: float = 0
        self.current_map = None
        pygame.init()
        pygame.display.set_caption(settings.GAME_TITLE)
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.screen: pygame.Surface = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.scene_manager: SceneManager = GameScene()

    def __del__(self):
        pass

    @staticmethod
    def get_events() -> [pygame.event.EventType]:
        return [event for event in pygame.event.get()]

    def start(self):
        self.run()

    def run(self):
        while self.scene_manager.scene is not None:
            self.scene_manager.handle_events(self.get_events())
            self.scene_manager.update(delta=self.delta_time)
            self.scene_manager.render()
            pygame.display.update()
            self.delta_time = self.clock.tick(settings.TICKRATE) / 1000.0


if __name__ == '__main__':
    ItechGame().start()
