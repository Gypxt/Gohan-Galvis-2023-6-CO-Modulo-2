import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import SHIELD_TYPE, AUTO_FIRE_TYPE, SPEED_TYPE


class BulletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []
        
        

    def update(self, game):
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)
            
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player' and not enemy.type =='enemy2':
                    game.enemy_manager.enemies.remove(enemy)
                    self.player_bullets.remove(bullet)
                    game.score.update()
                    
                elif enemy.type =='enemy2' and bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    self.player_bullets.remove(bullet)
                    game.enemy_manager.damage_durability += 1
                    
                    if game.enemy_manager.damage_durability == 4:
                        game.enemy_manager.enemies.remove(enemy)
                        game.enemy_manager.damage_durability = 0
                        game.score.count += 2
                   

        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.death_count.update()
                    game.leader_board.update(game.score.count)
                    game.playing =  False
                    pygame.time.delay(1000)
                    break
            elif bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy2':
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.death_count.update()
                    game.leader_board.update(game.score.count)
                    game.playing =  False
                    pygame.time.delay(1000)
                    break

        if game.player.has_powe_up and game.player.power_up_type == AUTO_FIRE_TYPE:
            if len(self.player_bullets) < 10000:
                
                bullet = Bullet(game.player)
                self.player_bullets.append(bullet)

        if game.player.has_powe_up and game.player.power_up_type == SPEED_TYPE:
            game.player.SPACESHIP_SPEED = 20
        else: 
            game.player.SPACESHIP_SPEED = 10


    def draw(self, screen):
        
        for bullet in self.player_bullets:
            bullet.draw(screen)

        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)

        if bullet.owner == 'enemy2' and len(self.enemy_bullets) < 6:
            self.enemy_bullets.append(bullet)

        if bullet.owner == 'player' and len(self.player_bullets) < 3:
            self.player_bullets.append(bullet)
    
    def reset(self):
        self.player_bullets = []
        self.enemy_bullets = []