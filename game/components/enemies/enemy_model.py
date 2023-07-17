import pygame
import random
from pygame. sprite import Sprite
from game.utils.constants import ENEMY_2

from game.utils.constants import  SCREEN_HEIGHT, SCREEN_WIDTH

class EnemyModel(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 10
    MOV_X = {0:'left', 1:'right'}

    def __init__(self, image):
        self.image = pygame.transform.scale(image, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.ENEMY_HEIGHT, SCREEN_WIDTH - self.ENEMY_WIDTH)
        self.rect.y = self.Y_POS
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.index = 0

    def update(self, ships):
        
        self.rect.y += self.speed_y

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()

                
        if self.rect.y >= SCREEN_HEIGHT :
            ships.remove(self)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))

    def change_movement_x(self):
        self.index += 1 
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.ENEMY_WIDTH) :
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10 ):
            self.movement_x = 'right'
            self.index = 0

