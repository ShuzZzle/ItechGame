from pygame import Surface
from pytmx import load_pygame


class MapLoader:

    def __init__(self):
        self.map_object = None
        self.layers = []

    def __del__(self):
        pass

    def load_map(self, path: str) -> Surface:
        self.map_object = load_pygame(path)

        for layer in self.map_object.layers:
            self.layers.append(layer)

        return self.map_object
