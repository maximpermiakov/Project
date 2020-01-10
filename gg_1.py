import pygame
import sys
import os
from pygame.locals import *
pygame.init()
# размеры окна:
size = width, height = 800, 600
clock = pygame.time.Clock()
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
FPS = 50
BACK = ['fon.png']
volume = None

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

all_sprites = pygame.sprite.Group()

def print_sprite(x, y, im):
    sprite_im = pygame.sprite.Sprite()
    sprite_im.image = load_image(im)
    sprite_im.rect = sprite_im.image.get_rect()
    all_sprites.add(sprite_im)
    sprite_im.rect.x = x
    sprite_im.rect.y = y
    return sprite_im


def terminate():
    pygame.quit()
    sys.exit()

def print_ss():
    fon = pygame.transform.scale(load_image(BACK[0]), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Новая игра", 1, (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)

def print_set():
    intro_text = ["Громкость",
                  "Яркость",
                  "Применить"]

    fon = pygame.transform.scale(load_image(BACK[0]), (width, height))
    screen.blit(fon, (0, 0))
    more_less_1 = ["+", "-"]
    font = pygame.font.Font(None, 30)
    k = 0
    for i in range(0, 200, 100):
        text = font.render(intro_text[k], 1, (100, 255, 100))
        text_x = width // 2 - text.get_width() // 2
        text_y = 20 - text.get_height() // 2 + i
        text_w = text.get_width()
        text_h = text.get_height()

        k += 1
        screen.blit(text, (text_x, text_y))

    text = font.render(intro_text[k], 1, (0, 255, 255))
    text_x = width // 2 - text.get_width() // 2
    text_y = 250 - text.get_height() // 2 + 300
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 255), (text_x - 10, text_y - 10,
                                                text_w + 20, text_h + 20), 1)



def start_screen():
    #sets = print_sprite(750, 550, "bugs.png")
    volume = print_sprite(750, 10, "volume.png")
    print_ss()
    sound = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 760 < event.pos[0] < 790  and 560 < event.pos[1] < 590 :
                    return 2
                elif 750 < event.pos[0] < 790 and 5 < event.pos[1] < 40:
                    if sound == 0:
                        all_sprites.remove(volume)
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        clock.tick(FPS)
                        all_sprites.update()
                        volume = print_sprite(750, 10, "voice_off.png")
                        all_sprites.update()
                        sound = 1
                    else:
                        all_sprites.remove(volume)
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        clock.tick(FPS)
                        all_sprites.update()
                        volume = print_sprite(750, 10, "volume.png")
                        all_sprites.update()
                        sound = 0
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)



def settings():
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("back4.png")
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    sprite.rect.x = 750
    sprite.rect.y = 550
    print_set()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 760 < event.pos[0] < 790  and 560 < event.pos[1] < 590 :
                    return 1
        screen.blit(fon, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

screens = 1
while True:
    if screens == 1:
        screens = start_screen()
    elif screens == 2:
        screens = settings()
    elif screens == 0:
        terminate()