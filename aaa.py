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