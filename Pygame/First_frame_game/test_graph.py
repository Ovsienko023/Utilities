import pygame
import sys


FPS = 40
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 64)


pygame.init()
main_window = pygame.display.set_mode((600, 400), pygame.RESIZABLE)


clock = pygame.time.Clock()  # fps


#  Paint in main window
# pygame.draw.rect(main_window, WHITE, (20, 20, 100, 75))

# #  Cross
# pygame.draw.aaline(main_window, BLACK, [20, 20], [120, 95])
# pygame.draw.aaline(main_window, BLACK, [20, 95], [120, 20])
# #  circle
# pygame.draw.circle(main_window, BLACK, (68, 57), 35, 2)


x = 0
pix = 1
color = WHITE

while True:
    main_window.fill(BLACK)

    clock.tick(FPS)  # fps
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # close window without error
'''
    pygame.draw.rect(main_window, color, (x, 20, 10, 10))
    pygame.display.update()

    
    
    if x == 50:
        x = 0
        color = GREEN

    else:
        x += pix
'''
    
    
