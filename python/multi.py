import pygame
import time

time.sleep(20)

WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.font.init()
myfont = pygame.font.SysFont("arial", 75)
label = myfont.render("in the mornings its fun but the evenings", 1, BLACK)
label2 = myfont.render("its not", 1, BLACK)
label3 = myfont.render("and i dont like it", 1, BLACK)

def draw():
    WIN.fill(WHITE)
    WIN.blit(label, (0, 150))
    WIN.blit(label2, (0, 250))
    WIN.blit(label3, (0, 350))
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True

        draw()
        time.sleep(20)
        run = False
    pygame.quit()

if __name__ == '__main__':
    main()
