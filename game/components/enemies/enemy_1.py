from game.components.enemies.enemy_model import EnemyModel
from game.utils.constants import ENEMY_1

class EnemyOne(EnemyModel) :
    def __init__(self):
        
        super().__init__(ENEMY_1)