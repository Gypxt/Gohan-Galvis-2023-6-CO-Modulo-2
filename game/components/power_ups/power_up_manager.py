import random

import pygame
from game.components.power_ups.auto_fire import AutoFire
from game.components.power_ups.more_speed import MoreSpeed
from game.components.power_ups.shield import Shield
from game.utils.constants import SPACESHIP_SHIELD


class PowerUpManager:
    POWER_UP_INITIAL_TIME = 10000
    POWER_UP_FINAL_TIME = 15000
    POWER_UP_TYPES = [Shield, AutoFire, MoreSpeed]
    
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(self.POWER_UP_INITIAL_TIME, self.POWER_UP_FINAL_TIME)
        self.duration = random.randint(3, 5)

    def generate_power_up(self):
        power_up_type = random.choice(self.POWER_UP_TYPES)
        power_up = power_up_type()
        self.power_ups.append(power_up)
        self.when_appears += random.randint( self.POWER_UP_INITIAL_TIME, self.POWER_UP_FINAL_TIME)

    def update(self, game):
        current_time = pygame.time.get_ticks()
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups )
            if game.player.rect.colliderect(power_up):
                
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_powe_up = True
                game.player.powe_time_up = power_up.start_time + (self.duration * 1000)
                if power_up.type == Shield.TYPE:
                    game.player.set_image((60, 75), SPACESHIP_SHIELD)
                self.power_ups.remove(power_up)
                self.powerup_sound_played = False

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        now = pygame.time.get_ticks()
        self.when_appears = random.randint(now + self.POWER_UP_INITIAL_TIME, now + self.POWER_UP_FINAL_TIME)

    