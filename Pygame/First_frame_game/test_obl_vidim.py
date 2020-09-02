import pygame

WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
BLACK = (0, 0, 0)


pygame.init()
main_window = pygame.display.set_mode((600, 400))

surf1 = pygame.Surface((100, 100))
surf1.fill(WHITE)
main_window.blit(surf1, (20, 20))
pygame.display.update()

pygame.draw.line(main_window, GREEN, (0, 35), (400, 35), 10)
pygame.display.update()

pygame.draw.line(surf1, RED, (0, 50), (400, 50), 10)
pygame.display.update()
print(surf1)
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    