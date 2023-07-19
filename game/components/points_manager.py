import pygame

from game.utils.constants import FONT_STYLE, SCREEN_WIDTH

class PointManager:
    MENU_COLOR = (255, 255, 255)
    def __init__(self):
        self.score = 0
        self.highest_score = 0
        self.highest_scores = [] 
        self.show_high_scores = False

    def update(self, points):
        self.score += points
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.update_highest_scores()
    
    def update_screen(self):
        pygame.display.update()

    def reset(self):
        self.score = 0

    def draw_score_in_game(self, screen):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (255, 255,255))
        text_rect= text.get_rect()
        text_rect.center = (1000, 50)
        screen.blit(text, text_rect)

    def update_highest_scores(self):

        self.highest_scores.append(self.highest_score)
        self.highest_scores.sort(reverse=True)

        # Mantiene solo los 10 puntajes más altos
        self.highest_scores = self.highest_scores[:10]

    def draw_high_scores(self, screen):
        screen.fill(self.MENU_COLOR)
        font = pygame.font.Font(FONT_STYLE, 30)
        y_position = 200 
        title_text = font.render("High Scores", True, (0, 0, 0))
        title_rect = title_text.get_rect()
        title_rect.center = (SCREEN_WIDTH // 2, y_position)
        screen.blit(title_text, title_rect)

        for i, score in enumerate(self.highest_scores, start=1):
            score_text = font.render(f"{i}. {score}", True, (0, 0, 0))
            score_rect = score_text.get_rect()
            score_rect.center = (SCREEN_WIDTH // 2, y_position + i * 40)
            screen.blit(score_text, score_rect)