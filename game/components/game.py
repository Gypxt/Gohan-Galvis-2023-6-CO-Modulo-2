import pygame
from game.components.game_over_menu import GameOverMenu
from game.components.points_manager import PointManager
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu

from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Spaceship()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu = Menu('Press \'S\' To Start...', self.screen)
        self.game_over = GameOverMenu(self.screen)
        self.running = False
        self.points = PointManager()
        
 
    def execute(self):
        self.running = True
        while self.running :
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()


    def run(self):
        # Game loop: events - update - draw
        self.game_reset()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False


    def update(self):
        self.player.update(self)
        self.enemy_manager.update(self.bullet_manager)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.points.draw_score_in_game(self.screen)
        if self.points.show_high_scores:
            self.points.draw_high_scores(self.screen)
        else:
            if not self.playing:
                self.show_menu()

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        
        self.menu.reset(self.screen)
        half_screen_whidth = SCREEN_WIDTH // 2
        if self.player.death_count > 0:
            
            self.game_over.update_message()  
            self.game_over.draw(self.screen)  
            self.game_over.desing_message(self.screen, f'Score: {self.points.score}', half_screen_whidth, 340)    
            self.game_over.desing_message(self.screen, f'Deaths: {self.player.death_count}', half_screen_whidth, 370)    
            self.game_over.desing_message(self.screen, f'Highest Score: {self.points.highest_score}', half_screen_whidth, 400) 
        else:
            self.menu.draw(self.screen)
        self.menu.update(self)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_h]:
            if not self.playing:
                self.points.show_high_scores = True
        elif keys[pygame.K_m]:
            self.points.show_high_scores = False
        elif keys[pygame.K_s]:
            if not self.playing:
                self.run()

    
    def game_reset(self):
        self.enemy_manager.reset()
        self.bullet_manager.reset()
        self.player.reset()
        self.points.reset()
        