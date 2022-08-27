import pygame

WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("team project!")
FPS = 60

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

p1 = 0
p2 = 0

pygame.font.init()
myfont = pygame.font.SysFont("arial", 75)
label = myfont.render(str(p1), 1, BLACK)
label2 = myfont.render(str(p2), 1, BLACK)

# functions
def draw():
    WIN.fill(WHITE)
    WIN.blit(label, (50, 50))
    WIN.blit(label2, (1100, 50))
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    global p1
                    p1 = 1

        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
