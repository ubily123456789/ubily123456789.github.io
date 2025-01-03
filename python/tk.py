import pygame
import os

WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("team project!")
FPS = 60

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# shuttle sizee
shuttlesizex, shuttlesizey = 16, 9
unit = 32
shuttledir = 45

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "team_picture")
background = pygame.image.load(os.path.join("Assets", "space.png"))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
earth = pygame.image.load(os.path.join("Assets", "earth.jpg"))
shuttle = pygame.image.load(os.path.join("Assets", "shuttle.jpg"))
shuttle = pygame.transform.rotate(pygame.transform.scale(shuttle, (shuttlesizex*unit, shuttlesizey*unit)), shuttledir)
shuttle.set_colorkey((12, 12, 12))


# coords
shuttlex = 100
shuttley = 100

# text
pygame.font.init()
myfont = pygame.font.SysFont("comicsans", 75)

# functions
def draw():
    shuttle.set_colorkey((12, 12, 12))
    WIN.blit(earth, (-100, -100))
    WIN.blit(shuttle, (shuttlex, shuttley))
    pygame.display.flip()

def move():
    global shuttlesizex
    global shuttledir
    global shuttlex
    global shuttley
    global unit
    keys_press = pygame.key.get_pressed()
    if keys_press[pygame.K_a]: shuttlex -= 7
    if keys_press[pygame.K_d]: shuttlex += 7
    if keys_press[pygame.K_w]: shuttley -= 7
    if keys_press[pygame.K_s]: shuttley += 7
    if keys_press[pygame.K_b]: shuttledir += 1
    if keys_press[pygame.K_n]: shuttlesizex += 1

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()
        move()

    pygame.quit()

if __name__ == "__main__":
    main()
