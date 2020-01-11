import pygame
import sys
import os
import random

pygame.init()
size = width, height = 900, 700
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("First_Step")
BACK = ["game_fon.jpg"] #фоны для разных уровней
heroes = ["copio", "corvo"]


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

game_fon = pygame.transform.scale(load_image(BACK[0]), (width, height))
screen.blit(game_fon, (0, 0))
font = pygame.font.Font(None, 50)
all_sprites = pygame.sprite.Group()
# все нужные переменные
x = 0
y = height - 207
side = True
speed = 5
sit = False
isJump = False
jumpCount = 8
run = True
left = False
right = False
right_s = True
left_s = False
animCount = 0
clock = pygame.time.Clock()

# функция для анимации
def drawWindow(k):
    global animCount, left, right, right_s, left_s

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
          load_image("corvo_3_left.png"), load_image("corvo_4_left.png"), load_image("corvo_5_left.png")]
corvo_s_r = load_image("corvo_4.png")
corvo_s_l = load_image("corvo_4_left.png")


hero_move = [(corvo_r, corvo_l)]
hero_stay = [(corvo_s_r, corvo_s_l)]

while run:
    clock.tick(35)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x > 0:
        left = True
        right = False
        x -= speed
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x < width - 50:
        left = False
        right = True
        x += speed
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]):
            sit = True
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]):
            isJump = True
    else:
        if jumpCount >= -8:
            if jumpCount < 0:
                y += (jumpCount**2) / 3
            else:
                y -= (jumpCount**2) / 3
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 8
    drawWindow(0)

pygame.quit()