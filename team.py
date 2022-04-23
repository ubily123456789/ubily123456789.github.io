# a project whith me and nathan!
import pygame
import random
import os

# getting the window
WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("team project!")
FPS = 60

# color var
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 200, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

aleinx, aleiny = 300, 500
border = pygame.Rect(595, 0, 10, HEIGHT)

# getting the picture and background
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "team_picture")
image = pygame.image.load(os.path.join(img_folder, "p2_jump.png")).convert()
image2 = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
background = pygame.image.load(os.path.join("Assets", "space.png"))

class enime():
    def ___init__(self, num):
        self.num = int(num)

new1 = enime()

# functions
def draw():
    WIN.blit(background, (0, 0))
    WIN.blit(image, (aleinx, aleiny))
    WIN.blit(image, (aleinx + 600, aleiny))
    pygame.draw.rect(WIN, BLACK, border)
    image.set_colorkey(BLACK)
    pygame.display.flip()

def move():
    keys_press = pygame.key.get_pressed()
    global aleinx
    global aleiny
    if keys_press[pygame.K_a] and aleinx - 5 > 0:
        aleinx -= 7

    if keys_press[pygame.K_d] and aleinx + 70 < border.x:
        aleinx += 7

    if keys_press[pygame.K_w] and aleiny - 5 > 0:
        aleiny -= 7

    if keys_press[pygame.K_s] and aleiny < HEIGHT - 100:
        aleiny += 7

def main():
    clock = pygame.time.Clock()
    alein = pygame.Rect(700, 300, 55, 40)
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
