import random
from game.components.enemies.enemy_model import EnemyModel
from game.utils.constants import ENEMY_2

class EnemyTwo(EnemyModel) :
    SPEED_Y = 7
    SPEED_X = 1
    def __init__(self):
        move_x_for = random.randint(50, 150)
        super().__init__(ENEMY_2, self.SPEED_X, self.SPEED_Y, move_x_for)
        self.move_y_for = random.randint(10, 50)
        self.index_y = 0
    
    def change_movement_x(self):
        super().change_movement_x()
        self.index_y += 1 
        if self.index_y >= self.move_y_for:
            self.speed_y = 0 if self.speed_y > 0 else self.SPEED_Y
            self.move_y_for = random.randint(50, 100) if self.speed_y == 0 else random.randint(10, 50)
            self.index_y = 0 

