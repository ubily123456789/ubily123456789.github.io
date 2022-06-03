# My baseball game :)
import pygame

# window stuff
WIDTH, HEIGHT = 950, 550
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("baseball game!")
FPS = 60

# the thing
x = 100
bat = pygame.Rect(x, 450, 200, 50)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOUR = (0, 222, 222)
YELLOW = (255, 255, 0)

# define functions
def move():
    global x
    keys_press = pygame.key.get_pressed()
    if keys_press[pygame.K_LEFT]:
        x = x+2

def draw():
    WIN.fill(BACKGROUND_COLOUR)
    pygame.draw.rect(WIN, BLACK, bat)
    pygame.display.flip()

# game loop
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        move()
        draw()


    pygame.quit()

if __name__ == "__main__":
    main()
