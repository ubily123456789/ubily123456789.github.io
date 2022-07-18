# My baseball game :)
import pygame
import random
import os

# window stuff
WIDTH, HEIGHT = 950, 550
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pong game!")
FPS = 60

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BACKGROUND_COLOUR = (0, 222, 222)

# coords
pltfrmx, pltfrmy = 100, 450
ballx, bally = 100, 100
yn = random.choice(["yes", "no"])
yn2 = random.choice(["yes", "no"])


# the thing
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "team_picture")
image = pygame.image.load(os.path.join(img_folder, "pong_pltfrm.png")).convert()
image = pygame.transform.scale(image, (300, 100))
image.set_colorkey(WHITE)
ball = pygame.image.load(os.path.join(img_folder, "circle.png")).convert()
ball = pygame.transform.scale(ball, (50, 50))
ball.set_colorkey(WHITE)

# ???
if yn == "yes":
    bdx = random.randrange(1, 5)
    bdx = bdx * 1.5
elif yn == "no":
    bdx = random.randrange(1, 5)
    bdx = bdx * 1.5
    bdxx = bdx * 2
    bdx = bdx - bdxx
if yn2 == "yes":
    bdy = random.randrange(1, 5)
    bdy = bdx * 1.5
elif yn2 == "no":
    bdy = random.randrange(1, 5)
    bdy = bdx * 1.5
    bdyy = bdx * 2
    bdy = bdy - bdyy

# define functions
def ballmove():
    global ballx
    global bally
    ballx += bdx
    bally += bdy

def ballmoveprt2():
    global bally
    global bdx
    if bally == 400:
        bdx = bdx - bdxx

def move():
    global pltfrmx
    global pltfrmy
    keys_press = pygame.key.get_pressed()
    if keys_press[pygame.K_RIGHT] and pltfrmx != WIDTH - 265:
        pltfrmx += 5
    if keys_press[pygame.K_LEFT] and pltfrmx != -50:
        pltfrmx -= 5

def draw():
    WIN.fill(BACKGROUND_COLOUR)
    WIN.blit(image, (pltfrmx, pltfrmy))
    WIN.blit(ball, (ballx, bally))
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
        ballmove()
        ballmoveprt2()
        draw()
        walls()

    pygame.quit()

if __name__ == "__main__":
    main()
