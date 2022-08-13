import pygame
import os

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong!")

FPS = 60
VELY = 5
VELX = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "team_picture")
ball = pygame.image.load(os.path.join(img_folder, "circle.png")).convert()
ball = pygame.transform.scale(ball, (70, 70))
ball.set_colorkey(WHITE)
image = pygame.image.load(os.path.join(img_folder, "pong_pltfrm.png")).convert()
image = pygame.transform.scale(image, (300, 100))
image.set_colorkey(WHITE)

# coords
ballx = 200
bally = 200
pltfrmx = 100
pltfrmy = 450

# define functions
def draw():
    WIN.fill(CYAN)
    WIN.blit(ball, (ballx, bally))
    WIN.blit(image, (pltfrmx, pltfrmy))
    pygame.display.flip()

def move():
    global pltfrmx
    global pltfrmy
    keys_press = pygame.key.get_pressed()
    if keys_press[pygame.K_RIGHT] and pltfrmx < WIDTH - 265:
        pltfrmx += 7
    if keys_press[pygame.K_LEFT] and pltfrmx > -50:
        pltfrmx -= 7

def move2():
    global ballx
    global bally
    ballx += VELX
    bally -= VELY

def walls():
    global bally
    global ballx
    global VELY
    global VELX
    if bally == 0:
        VELY -= VELY * 2
    if ballx == 830:
        VELX -= VELX * 2 # ballx > pltfrmx - 150
    if bally == 430 and ballx :
        VELY -= VELY * 2
    if ballx == 0:
        VELX -= VELX * 2

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
        move2()
        walls()

    pygame.quit()

if __name__ == "__main__":
    main()
