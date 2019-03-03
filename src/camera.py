import pygame
import settings


class Camera:

    def __init__(self, pos: pygame.Vector2):
        self.camera = pos
        # This is the viewing Area, also known as the Screen Size
        # self.cameraRect = pygame.Rect(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
