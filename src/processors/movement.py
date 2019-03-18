from src import esper
from src.components.position import Position
from src.components.velocity import Velocity
import typing


class MovementProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self, deltatime, *args, **kwargs):
        for entity, (vel, pos) in self.world.get_components(Velocity, Position):
            vel: Velocity = vel
            pos: Position = pos
            pos.x = vel.velx * deltatime
