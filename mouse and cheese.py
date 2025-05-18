from pygame import *
from random import randint

window = display.set_mode((700, 500))
display.set_caption('Мышь и сыр')
stol = transform.scale(image.load("stol.jpg"), (700, 500))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= 5
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += 5 
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 5
        if keys_pressed[K_DOWN] and self.rect.y < 435:
            self.rect.y += 5

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(0, 635)

# Инициализация
font.init()
font1 = font.Font(None, 36)

player = Player('mish.png', 200, 400, 2)
monsters = sprite.Group()

for i in range(3):
    enemy = Enemy('sir.jpg', randint(0, 635), randint(-100, 0), 2)
    monsters.add(enemy)

game = True
while game:
    window.blit(stol, (0, 0))
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    # Проверка столкновений
    if sprite.spritecollide(player, monsters, False):
        for m in monsters:
            if sprite.collide_rect(player, m):
                m.kill()
        
    
    # Обновление и отрисовка всех спрайтов
    player.update()
    player.reset()
    
    monsters.update()
    monsters.draw(window)
    
    display.update()
    clock.tick(60)