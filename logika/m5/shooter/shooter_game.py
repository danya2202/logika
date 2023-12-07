#Створи власний Шутер!
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

win_width = 700
win_height = 500

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play(-1)

class GameSprite(sprite.Sprite):
    def __init__(self, image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = scale(load(image), (65, 65))
        self.speed = player_speed
        self.width = player_width
        self.height = player_height
        
        self.rect = self.image.get_rect()

        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_RIGHT] and self.rect.y > 5:
            self.rect.x += self.speed
        if keys[K_LEFT] and self.rect.y < win_width - 80:
            self.rect.x -= self.speed
    def shoot(self):
        pass
    
rocket = Player('rocket.png', 5, win_height-80, 4, 4, 4)    



window = display.set_mode((win_width, win_height))

background = scale(load('galaxy.jpg'), (win_width, win_height))

game = True
finish = False

clock = time.Clock()

FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if not finish:
            window.blit(background, (0, 0))
            rocket.reset()
            
            
            
            
            
            
            rocket.update()
    
    display.update()
    clock.tick(FPS)