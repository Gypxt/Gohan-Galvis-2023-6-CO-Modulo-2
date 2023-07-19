from game.components.menu import Menu
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH


class GameOverMenu(Menu):
    MESSAGE = 'Game over. Press \'S\' to restart.'
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2 
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    def __init__(self, screen):
       
        super().__init__(self.MESSAGE , screen)

    def update_message(self):
        self.text = self.font.render(self.MESSAGE, True, self.MESSAGE_COLOR)
        self.text_rect= self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT )

    def desing_message(self, screen, message, pos_x = HALF_SCREEN_WIDTH, pos_y = HALF_SCREEN_HEIGHT, color = (0,0,0)):
        text = self.font.render(message, True, color)
        text_rect= text.get_rect()
        text_rect.center = (pos_x, pos_y)
        screen.blit(text, text_rect)
    