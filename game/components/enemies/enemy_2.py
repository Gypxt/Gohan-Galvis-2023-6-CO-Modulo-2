from game.components.enemies.enemy_model import EnemyModel
from game.utils.constants import ENEMY_2, SCREEN_HEIGHT

class EnemyTwo(EnemyModel) :
    is_actuali = True
    def __init__(self):
        super().__init__(ENEMY_2)
    