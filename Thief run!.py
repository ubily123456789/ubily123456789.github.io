import pygame
import os

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Thief run!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)

YELLOW_SHIP = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SHIP, (55, 40)), 90)

def draw():
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SHIP, (100, 300))
    pygame.display.flip()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()
    pygame.quit()

if __name__ == "__main__"
    main()
