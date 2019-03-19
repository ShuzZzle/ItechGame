import pygame

from src.entity import Entity
from src.esper import World


class Player:

    def __init__(self, world: World, player_name: str = "N.A."):
        self.entity_id: int = None
        self.player_name = player_name
        self.world = world
        self.player = self.world.create_entity()

    def create(self, *components):
        if self.entity_id is None:
            self.entity_id = self.world.create_entity()
            for component in components:
                self.world.add_component(self.entity_id, component)

    def get_entity_id(self):
        return self.entity_id


