import pygame

FPS = 40
W = 600
H = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 64)

pygame.init()
main_window = pygame.display.set_mode((W, H), pygame.RESIZABLE)

clock = pygame.time.Clock()

x = W // 2
y = H // 2

r = 40

while True:
    main_window.fill(WHITE)
    pygame.draw.circle(main_window, BLACK, (x, y), r)
    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 3
    elif keys[pygame.K_RIGHT]:
        x += 3
    elif keys[pygame.K_UP]:
        y -= 3
    elif keys[pygame.K_DOWN]:
        y += 3     
    clock.tick(FPS)