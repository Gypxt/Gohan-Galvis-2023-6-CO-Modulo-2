import pygame
import os
pygame.init() 

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
SPEEDPOWER = pygame.image.load(os.path.join(IMG_DIR, 'Other/more_speed.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
AUTO_FIRE_TYPE = 'Auto fire'
SPEED_TYPE = 'more speed'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_POWER = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_4.png"))


BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))

FONT_STYLE = 'freesansbold.ttf'

SOUND_GAMEOVER = pygame.mixer.Sound(os.path.join(IMG_DIR,'Sounds/Game_Over_sound_effect.wav'))
MUSIC_GAME = pygame.mixer.Sound(os.path.join(IMG_DIR,'Sounds/Music_Game.wav'))
TAKE_POWER_UP = pygame.mixer.Sound(os.path.join(IMG_DIR,'Sounds/PowerUp_Sound_Effect.wav'))
LASER_BULLET = pygame.mixer.Sound(os.path.join(IMG_DIR,'Sounds/Space_Laser_sound_effect.wav'))
EXPLOSION = pygame.mixer.Sound(os.path.join(IMG_DIR,'Sounds/Retro_Explosion_Sound_Effect.wav'))

pygame.mixer.Sound.set_volume(SOUND_GAMEOVER, 0.2)
pygame.mixer.Sound.set_volume(MUSIC_GAME, 0.2)
pygame.mixer.Sound.set_volume(TAKE_POWER_UP, 0.2)
pygame.mixer.Sound.set_volume(LASER_BULLET, 0.2)
pygame.mixer.Sound.set_volume(EXPLOSION, 0.2)