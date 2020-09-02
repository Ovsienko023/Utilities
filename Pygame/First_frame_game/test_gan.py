import pygame


WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
BLACK = (0, 0, 0)

pygame.init()
main_window = pygame.display.set_mode((600, 400))
main_window.fill(WHITE)
pygame.display.update()

y = 365
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pygame.draw.circle(main_window, BLACK, i.pos, 5)
                pygame.display.update()
                x = i.pos[0]
                coordinat = i.pos
                print(i.pos)
                while y != coordinat[1] + 1:
                        main_window.fill(WHITE)
                        pygame.draw.circle(main_window, BLACK, (x, y), 35, 2)
                        y -= 1
                        pygame.display.update()
                        pygame.time.delay(20)
                        print(x, y)

                pygame.draw.circle(main_window, RED, coordinat, 50, 20)
                pygame.display.update()
                y = 365
    pygame.time.delay(20)
