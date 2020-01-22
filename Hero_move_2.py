import pygame
import sys
import os
import random


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
size = width, height = 900, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption("First_Step")
BACK = ["game_fon.jpg", "game_fon_1.jpg"]  # фоны для разных уровней
heroes_stats = [(1000, 120, 4, 300), (700, 70, 6, 500)]  # здоровье, урон, скорость, стамина
corvo_bull = load_image("corvo_bul.png")
corvo_bull = pygame.transform.scale(corvo_bull, (20, 40))
copio_bull = load_image("copio_bull.png")
copio_bull = pygame.transform.scale(copio_bull, (20, 10))
bullet_img = [corvo_bull, copio_bull]
bul_v = [10, 15]
k = 0


def terminate():
    pygame.quit()
    sys.exit()


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 8

    def move(self):
        self.x += self.speed
        if self.x <= width:
            screen.blit(corvo_bull, (self.x, self.y))
            return True
        else:
            return False


def print_text(mess, x, y, font_color, font_size=40):
    font_type = pygame.font.Font(None, font_size)
    text = font_type.render(mess, True, font_color)
    t_w = text.get_width()
    t_h = text.get_height()
    screen.blit(text, (x, y))


def bul_move(x, y, bul_speed, mass):
    mass.append(bullet_img[k])
    if 0 < x < width:
        for i in mass:
            if left or left_s:
                screen.blit(i, (x, y + 20))
                x -= bul_speed
            elif right or right_s:
                screen.blit(i, (x + 50, y + 20))
                x += bul_speed
            if x <= 0 or x >= width:
                mass.remove(i)


n = 0
game_fon = pygame.transform.scale(load_image(BACK[n]), (width, height))
screen.blit(game_fon, (0, 0))
font = pygame.font.Font(None, 50)
all_sprites = pygame.sprite.Group()
# все нужные переменные
x = 0
y = height - 207
bul_x = x
bul_y = y
side = True
sit = False
isJump = False
jumpCount = 8
run = True
left = False
right = True
right_s = True
left_s = False
fire = False
animCount = 0
weapon = False
clock = pygame.time.Clock()
tp_rad = 50


# функция для анимации
def drawWindow():
    global animCount, left, right, right_s, left_s, k

    screen.blit(game_fon, (0, 0))
    if animCount + 1 >= 25:
        animCount = 0

    if left:
        left_s = True
        right_s = False
        screen.blit(hero_move[k][1][animCount // 5], (x, y))
        animCount += 1
    elif right:
        right_s = True
        left_s = False
        screen.blit(hero_move[k][0][animCount // 5], (x, y))
        animCount += 1
    else:
        if right_s:
            screen.blit(hero_stay[k][0], (x, y))
        if left_s:
            screen.blit(hero_stay[k][1], (x, y))
    if fire and 0 <= bul_x <= width:
        corvo_bull = load_image("corvo_bul.png")
        corvo_bull = pygame.transform.scale(corvo_bull, (20, 40))
        copio_bull = load_image("copio_bull.png")
        copio_bull = pygame.transform.scale(copio_bull, (20, 10))
        bullet_img = [corvo_bull, copio_bull]
        all_btn_bullets.append(bullet_img[k])
        for bullet in all_btn_bullets:
            screen.blit(bullet, (bul_x + 15, bul_y + 30))

    print_text(str(heroes_stats[k][0]), 10, 5, (255, 0, 0))
    pygame.display.update()


def print_sprite(x, y, im):
    sprite_im = pygame.sprite.Sprite()
    sprite_im.image = load_image(im)
    sprite_im.rect = sprite_im.image.get_rect()
    all_sprites.add(sprite_im)
    sprite_im.rect.x = x
    sprite_im.rect.y = y
    return sprite_im


corvo_r = [load_image("corvo_1.png"), load_image("corvo_2.png"),
           load_image("corvo_3.png"), load_image("corvo_4.png"),
           load_image("corvo_5.png")]
corvo_l = [load_image("corvo_1_left.png"), load_image("corvo_2_left.png"),
           load_image("corvo_3_left.png"), load_image("corvo_4_left.png"),
           load_image("corvo_5_left.png")]
corvo_s_r = load_image("corvo_4.png")
corvo_s_l = load_image("corvo_4_left.png")
copio_r = [load_image("copio_1.png"), load_image("copio_2.png"),
           load_image("copio_3.png"), load_image("copio_4.png"), load_image("copio_1.png")]
copio_l = [load_image("copio_1_left.png"), load_image("copio_2_left.png"),
           load_image("copio_3_left.png"), load_image("copio_4_left.png"),
           load_image("copio_1_left.png")]
copio_s_r = load_image("copio_1.png")
copio_s_l = load_image("copio_1_left.png")
hero_move = [(corvo_r, corvo_l), (copio_r, copio_l)]
hero_stay = [(corvo_s_r, corvo_s_l), (copio_s_r, copio_s_l)]
jp = heroes_stats[k][3]
hp = heroes_stats[k][0]
damage = heroes_stats[k][1]
speed = heroes_stats[k][2]
all_btn_bullets = []
down = True
while run:
    clock.tick(35)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        bul_x = x
        bul_y = y

    if keys[pygame.K_1]:
        k = 0
    if keys[pygame.K_2]:
        k = 1
    if keys[pygame.K_9]:
        n = 0
    if keys[pygame.K_0]:
        n = 1
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_x:
            all_btn_bullets.append(bullet_img[k])
            bul_x, bul_y = x, y
            fire = True
            for bullet in all_btn_bullets:
                if bul_x <= 0 or bul_x >= width - 15:
                    all_btn_bullets.remove(bullet)

    if right or right_s:
        bul_x += bul_v[k]
    elif left or left_s:
        bul_x -= bul_v[k]

    if event.type == pygame.MOUSEBUTTONDOWN:
        print(event)

    if keys[pygame.K_ESCAPE]:
        terminate()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x > 0:
        left = True
        right = False
        x -= speed
        if keys[pygame.K_e] and jp >= 300:
            if tp_rad <= x:
                x -= tp_rad
            else:
                x = 0
            jp = -200
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x < width - 50:
        left = False
        right = True
        x += speed
        if keys[pygame.K_e] and jp >= heroes_stats[k][3]:
            if x <= width - tp_rad:
                x += tp_rad
            else:
                x = width - 50
            jp = -200
    else:
        left = False
        right = False
        animCount = 0

    if jp <= 0:
        isJump = False
        lost = False

    if jp >= 200:
        lost = True

    if not (isJump):
        if jp <= heroes_stats[k][3]:
            jp += 5
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]):
            sit = True
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and lost:
            isJump = True
            jp -= 100

    elif isJump and jp > 0:
        if jumpCount >= -8:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 3
            else:
                y -= (jumpCount ** 2) / 3
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 8
    drawWindow()

pygame.quit()
