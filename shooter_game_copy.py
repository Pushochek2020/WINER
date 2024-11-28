from pygame import *
from random import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.rect = self.rect.inflate(-65, -3)
    def reset(self):
        window.blit(self.image , (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 145:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 340:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 10:
            self.speed -= 2
            self.rect.y -= self.speed
            self.speed += 2
        if keys[K_s] and self.rect.y < 680:
            self.speed -= 3
            self.rect.y += self.speed
            self.speed += 3
            

class Enemy(GameSprite):
    def update(self):
        for i in range(3):
            sprite.Sprite.__init__(self)
            self.image = transform.scale(image.load(player_image), (size_x, size_y))
            self.speed = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
        def dvij():
            self.rect.y -= self.speed
        def reset(self):
            window.blit(self.image , (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = choice(spisok)
            self.rect.y = 0
            lost = lost + 1

img_phon = 'doroga.jpg'
img_pleer = 'car_pleer.png'
img_enemy = 'enemy.png'
img_konec = 'konec.png'

spisok = [280, 460, 635, 820]

FPS = 60
clock = time.Clock()

win_width = 1200
win_height = 900
window = display.set_mode((win_width, win_height))
display.set_caption('Гонки')
background = transform.scale(image.load(img_phon), (win_width, win_height))
x = 0
y = 0
speed = 5
lost = 0
max_lost = 10

enemys = sprite.Group()

font.init()
font1 = font.Font(None, 120)
font2 = font.Font(None, 80)
win = font1.render('WIN!', True, (255, 255, 255))
lose = font1.render('LOSE!', True, (180, 0, 0))

for i in range(1, 4):
    enemy = Enemy(img_enemy, randint(280, win_width - 80), 220, 105, 175, 7)
    enemys.add(enemy)

pleer = Player(img_pleer, 410, win_height - 220, 200, 220, speed)




konec = False
igra = True
while igra:
    for e in event.get():
        if e.type == QUIT:
            igra = False

    y += speed

    if y >= win_height:
        y = 0

    

    if not konec:
        window.blit(background, (x, y))
        window.blit(background, (x, y - win_height))

        pleer.update()
        enemys.update()
        
        if sprite.spritecollide(pleer, enemys, False):
            konec = True 
            rer = transform.scale(image.load(img_konec), (200,200))
            window.blit(rer, (x, y))

        if lost >= max_lost:
            konec = True 
            window.blit(win, (200, 200))

        pleer.reset()
        enemys.draw(window)

        text = font2.render('Счёт:' + str(lost), 1, (255,255,255))
        window.blit(text, (10, 20))

        display.update()
    else:
        konec = False
        lost = 0
        
        for m in enemys:
            m.kill()

        time.delay(3000)
        for i in range(1, 4):
            enemy = Enemy(img_enemy, randint(280, win_width - 80), 220, 105, 175, 7)
            enemys.add(enemy)

    clock.tick(FPS)
    display.update()