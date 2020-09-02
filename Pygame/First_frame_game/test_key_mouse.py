import pygame


WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)

pygame.init()
main_window = pygame.display.set_mode((400, 300))
main_window.fill(WHITE)
pygame.display.update()


while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pygame.draw.circle(main_window, RED, i.pos, 20)
                pygame.display.update()
            elif i.button == 2:
                main_window.fill(WHITE)
                pygame.display.update()
    pygame.time.delay(20)

pygame.MOUSE