# Kenneth

import pygame
import os
pygame.font.init()

FONT = pygame.font.SysFont('comicsans', 100)

SCREENX = 1700
SCREENY = 900

WHITE = (255, 255, 255)

x = 0
TEXT = FONT.render(str(x), 1, (255, 255, 255))

WIN = pygame.display.set_mode((SCREENX, SCREENY))
BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (SCREENX, SCREENY))


def draw_window():
    WIN.blit(BACKGROUND, (0, 0))
    TEXT = FONT.render(str(x), 1, (255, 255, 255))
    WIN.blit(TEXT, ((SCREENX - TEXT.get_width()) /
         2, (SCREENY - TEXT.get_height()) / 2))
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    global x
                    x += 1

        draw_window()
    pygame.quit


if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------------------------------------------



# Philip

# Grade
