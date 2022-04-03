#создай игру "Лабиринт"!
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y =player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed= key.get_pressed()
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x  += 5
        if keys_pressed[K_a] and self.rect.x  > 5:
            self.rect.x  -= 5
        if keys_pressed[K_s] and self.rect.y  < 395:
            self.rect.y  += 5
        if keys_pressed[K_w] and self.rect.y  > 5:
            self.rect.y -= 5
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 100:
            self.direction = "right"
        if self.rect.x >= 300:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_height, wall_width):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill([color_1, color_2, color_3])
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
hero = Player("hero.png", 2, 300, 2 )
cyborg = Enemy("cyborg.png", 60, 150, 2)
wall1 = Wall(0,240,0, 200, 100, 20, 300)
wall2 = Wall(0,240,0, 200, 350, 20, 400)
wall3 = Wall(0,240,0, 500, 300, 400, 20)
wall4 = Wall(0, 240,0, 180, 10, 110, 20)

gold = GameSprite("treasure.png", 200, 30, 2)
window = display.set_mode((700,500))
display.set_caption("Джунгли")
background = transform.scale(image.load("background.jpg"), (700, 500))
font.init()
font = font.Font(None, 70)
win = font.render('You Win', True, (215,215,0))
win1 = font.render('You Lose', True, (215,0,0))
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
clock = time.Clock() 
FPS = 100 
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
finish = False
game = True
while game:
    if finish != True:
        window.blit(background,(0, 0))
        if sprite.collide_rect(hero, gold):
            finish = True
            window.blit(win, (200,200))
            money.play()
        if sprite.collide_rect(hero, cyborg):
            finish = True
            window.blit(win1, (200,200))
            kick.play()
        if sprite.collide_rect(hero, wall1):
            finish = True
            window.blit(win1, (200,200))
            kick.play()
        if sprite.collide_rect(hero, wall2):
            finish = True
            window.blit(win1, (200,200))
            kick.play()
        if sprite.collide_rect(hero, wall3):
            finish = True
            window.blit(win1, (200,200))
            kick.play()
        if sprite.collide_rect(hero, wall4):
            finish = True
            window.blit(win1, (200,200))
            kick.play()
        
        
        hero.reset()
        hero.update()
        cyborg.reset()
        cyborg.update()
        gold.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)



