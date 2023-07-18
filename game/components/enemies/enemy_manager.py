import random
from game.components.enemies.enemy_model import EnemyModel
from game.components.enemies.enemy_1 import EnemyOne
from game.components.enemies.enemy_2 import EnemyTwo

class EnemyManager:

    def __init__(self):
        self.enemies = []
        


    def update(self, bullet_manager):

        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, bullet_manager)
            

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):

        if len(self.enemies) < 1:

            enemy_type = random.randint(1, 2)
            if enemy_type == 1:
                enemy = EnemyOne()
            else:
                enemy = EnemyTwo()

            self.enemies.append(enemy)