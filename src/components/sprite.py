from pygame.sprite import Sprite as PygameSprite


class Sprite:
    def __init__(self, sprite: PygameSprite):
        self.sprite: PygameSprite = sprite
