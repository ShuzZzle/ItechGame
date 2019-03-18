import pygame

from src.entity import Entity


class Player:

    def __init__(self, entity_id, player_name="N.A."):
        self.entity_id = entity_id
        self.player_name = player_name

    def get_entity_id(self):
        return self.entity_id


