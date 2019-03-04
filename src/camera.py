import pygame
import settings


class Camera:

    def __init__(self):
        # This is the viewing Area, also known as the Screen Size
        self.camera = pygame.Rect(0, 0, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
