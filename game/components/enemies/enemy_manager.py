import random
from game.components.enemies.enemy_model import EnemyModel
from game.components.enemies.enemy_1 import EnemyOne
from game.components.enemies.enemy_2 import EnemyTwo

class EnemyManager:
    firs_enemy =  EnemyOne()
    second_enemy =  EnemyTwo()

    def __init__(self):
        self.enemies = []
        self.model = {0: self.firs_enemy.image, 1: self.second_enemy.image}


    def update(self):

        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies)
            

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):

        if len(self.enemies) < 1:

            enemy_type = random.randint(0, 1)
            enemy = EnemyModel(self.model[enemy_type])

            if enemy_type == 1:  
                enemy.speed_y = 5  
                enemy.speed_x = 10  

            self.enemies.append(enemy)