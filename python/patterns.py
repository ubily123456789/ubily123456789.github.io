import pygame as pg
import os

WIDTH, HEIGHT = 1200, 600
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Philip's first pygame game")
FPS = 60
VEL = 8

# coords
rshipx, rshipy = 975, 100
yshipx, yshipy = 100, 100

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIME = (0, 255, 0)

YSHIP = pg.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YSHIP = pg.transform.rotate(pg.transform.scale(YSHIP, (100, 80)), 90)
RSHIP = pg.image.load(os.path.join("Assets", "spaceship_red.png"))
RSHIP = pg.transform.rotate(pg.transform.scale(RSHIP, (100, 80)), 270)

def draw():
    WIN.fill(LIME)
    WIN.blit(YSHIP, (yshipx, yshipy))
    WIN.blit(RSHIP, (rshipx, rshipy))
    pg.draw.rect(WIN, BLACK, pg.Rect(WIDTH/2-10, 0, 10, HEIGHT))
    pg.display.flip()

def bound():
    global YSHIP
    if YSHIP.right == WIDTH/2-10:
        print("hello world")

def move():
    global yshipx; global yshipy
    global rshipx; global rshipy
    key = pg.key.get_pressed()
    if key[pg.K_a]: yshipx -= VEL
    if key[pg.K_d]: yshipx += VEL
    if key[pg.K_s]: yshipy += VEL
    if key[pg.K_w]: yshipy -= VEL
    if key[pg.K_LEFT]: rshipx -= VEL
    if key[pg.K_RIGHT]: rshipx += VEL
    if key[pg.K_DOWN]: rshipy += VEL
    if key[pg.K_UP]: rshipy -= VEL

def main():
    clock = pg.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        draw()
        move()
        bound()

    pg.quit()

if __name__ == "__main__":
    main()
