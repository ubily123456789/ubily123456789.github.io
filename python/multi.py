# a game for me and Philip
import pygame
import maths

# window stuff
WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("K & P")
FPS = 60

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# score
a = ""
k = 0
p = 0
p_l = 1
k_l = 199

# text
pygame.font.init()
myfont = pygame.font.SysFont("comicsans", 75)
k_s = myfont.render(str(k), 1, BLACK)
p_s = myfont.render(str(p), 1, BLACK)
psn = myfont.render(str(a), 1, BLACK)

def draw():
    p_s = myfont.render(str(p), 1, BLACK)
    k_s = myfont.render(str(k), 1, BLACK)
    psn = myfont.render(str(a), 1, BLACK)
    WIN.fill(WHITE)
    WIN.blit(k_s, (50, 50))
    WIN.blit(p_s, (840, 50))
    WIN.blit(psn, (500, 250))
    pygame.display.flip()

def end():
    global k
    global p
    global a
    if k > 99: a = "Big bro Won!"; p = 0; k = 100
    if p > 99: a = "Philip Won!"; k = 0; p = 100

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            global p_l
            global p
            global k
            global k_l
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l: p += 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: k += 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s: k += 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s: k += 1

        draw()
        end()

    pygame.quit()

if __name__ == "__main__":
    main()
