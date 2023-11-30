#створи гру "Лабіринт"!
from pygame import *
from pygame.sprite import collide_rect
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, image, x, y, speed):
        super().__init__()
        self.image = scale(load(image), (65, 65))
        self.speed = speed
        
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > win_height - 500:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y > 5:
            self.rect.x += self.speed
        if keys[K_LEFT] and self.rect.y < win_width - 80:
            self.rect.x -= self.speed
            
            
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x >= 620:
            self.direction = 'left'
            
        
class Wall(sprite.Sprite):
    def __init__(self, wall_x, wall_y, wall_width, wall_height):
        super().__init__()   
        self.width = wall_width
        self.height = wall_height
        
        self.image = Surface((self.width, self.height))
        self.image.fill((0, 255, 0))
                 
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))      
            
win_width = 700
win_height = 500

window = display.set_mode((700, 500))

background = scale(load('background.jpg'), (win_width, win_height))

player = Player('hero.png', 5, 420, 4)
monster = Enemy('cyborg.png', 620, 300, 2)

treasure = GameSprite('treasure.png', 620, 420, 0)

wall_1 = Wall(150, 150, 25, 250)
wall_2 = Wall(250, 200, 25, 190)



walls = [wall_1, wall_2]

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
f = font.Font(None, 70)

win = f.render('YOU WIN!', True, (255, 215, 0))
lose = f.render('YOU LOSE!',False, (255, 0, 0))
mixer.init()
mixer.music.load("jungles.ogg")

money_sound = mixer.Sound('money.ogg')
kick_sound = mixer.Sound('kick.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        
        window.blit(background, (0, 0))        
        player.reset()        
        monster.reset()        
        treasure.reset()        
        for wall in walls:
            wall.reset()    
        player.update()        
        monster.update()        
            
        if sprite.collide_rect(player, treasure):    
            finish = True
            window.blit(win, (250, 250))
            money_sound.play()
        
        if sprite.collide_rect(player, monster):    
            finish = True
            window.blit(lose, (250, 250))
            kick_sound.play()
        
        for wall in walls:
            if sprite.collide_rect(player, wall):    
                finish = True
                window.blit(lose, (250, 250))
                kick_sound.play()
            
         
    display.update()
    clock.tick(FPS)