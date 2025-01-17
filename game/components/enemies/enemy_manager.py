import random
from game.components.enemies.enemy_model import EnemyModel
from game.components.enemies.enemy_1 import EnemyOne
from game.components.enemies.enemy_2 import EnemyTwo
from game.components.enemies.enemy_3 import EnemyTree

class EnemyManager:

    def __init__(self):
        self.enemies = []
        self.damage_durability = 0
        


    def update(self, bullet_manager):

        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, bullet_manager)
            

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):

        if len(self.enemies) < 1:

            enemy_type = random.randint(1, 3)
            if enemy_type == 1:
                enemy = EnemyOne()
            elif enemy_type == 2:
                enemy = EnemyTwo()
            else:
                enemy = EnemyTree()

            self.enemies.append(enemy)

    def reset(self):
        self.enemies = []
        self.damage_durability = 0