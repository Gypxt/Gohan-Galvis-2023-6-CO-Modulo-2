from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SPEEDPOWER, SPEED_TYPE


class MoreSpeed(PowerUp):
    TYPE = SPEED_TYPE
    def __init__(self):
        super().__init__(SPEEDPOWER, SPEED_TYPE)