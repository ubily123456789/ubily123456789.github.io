# My baseball game :)
import pygame

# window stuff
WIDTH, HEIGHT = 950, 550
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("baseball game!")
FPS = 60

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# define functions
def draw():
    WIN.fill(WHITE)
    pygame.display.flip()

# game loop
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
