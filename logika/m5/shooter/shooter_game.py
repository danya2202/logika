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

fire_sound = mixer.Sound('fire.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self, image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = scale(load(image), (player_width, player_height))
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
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)
        
        
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y>win_height:
            self.rect.y=0
            self.rect.x=randint(0, win_width-80)
            lost = lost + 1
            print(lost)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
b1 = Bullet('bullet.png', 350, 350, 15, 20, 15)           
    
rocket = Player('rocket.png', 5, win_height-80, 80, 100, 4)    

bullets = sprite.Group()


monsters = sprite.Group()
for i in range(5):
    mon = Enemy('ufo.png', randint(0, win_width-80), 0, 80, 50, randint(1, 5))
    monsters.add(mon)
    
font.init()
font1 = font.SysFont('Arial', 36)



window = display.set_mode((win_width, win_height))

background = scale(load('galaxy.jpg'), (win_width, win_height))

game = True
finish = False

clock = time.Clock()
lost = 0
score = 0
FPS = 60


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
               rocket.fire() 
               fire_sound.play()
    if not finish:
        window.blit(background, (0, 0))
        rocket.reset()
        txt_lose = font1.render(f'Пропущено: {lost}', True, (255,255,255))
        window.blit(txt_lose, (10, 50))
        
        txt_win = font1.render(f'Рахунок: {score}', True, (255,255,255))
        window.blit(txt_win, (10, 10))
        
        monsters.draw(window)
        monsters.update()    
            
        bullets.draw(window)
        bullets.update()           
            
            
        rocket.update()
    
    display.update()
    clock.tick(FPS)