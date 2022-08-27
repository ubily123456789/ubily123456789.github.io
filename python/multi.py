import pygame

WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("K & P")
FPS = 60

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# score
k = 0
p = 0

def draw():
    WIN.fill(WHITE)
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
                if event.key == pygame.K_a:
                    global p
                    p += 1
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
