# a game for me and Philip
import pygame

# window stuff
WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("K & P")
FPS = 60

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# score
a = 0
k = 0
p = 0

# text
pygame.font.init()
myfont = pygame.font.SysFont("comicsans", 75)
k_s = myfont.render(str(k), 1, BLACK)
p_s = myfont.render(str(p), 1, BLACK)

def draw():
    p_s = myfont.render(str(p), 1, BLACK)
    k_s = myfont.render(str(k), 1, BLACK)
    WIN.fill(WHITE)
    WIN.blit(k_s, (50, 50))
    WIN.blit(p_s, (1100, 50))
    pygame.display.flip()

def score():
    pass

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l: global p; p += 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: global k; k += 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s: k += 2
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
