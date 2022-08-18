# a baseball game with me and philip
import pygame
import os

WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my game!")

FPS = 60
aleinx, aleiny = 100, 100

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "team_picture")
image = pygame.image.load(os.path.join(img_folder, "p2_jump.png")).convert()
image.set_colorkey(BLACK)

# borders
border = pygame.Rect(0, 0, 1200, 20)
borderup = pygame.Rect(0, 580, 1200, 20)
borderleft = pygame.Rect(0, 0, 20, 600)
borderright = pygame.Rect(1180, 0, 20, 600)


# define functions
def move():
    global aleinx
    global aleiny
    keys_press = pygame.key.get_pressed()
    if keys_press[pygame.K_a] and aleinx - 5 > 0: aleinx -= 7
    if keys_press[pygame.K_d] and aleinx + 70 < borderright.x: aleinx += 7
    if keys_press[pygame.K_w] and aleiny - 5 > 0: aleiny -= 7
    if keys_press[pygame.K_s] and aleiny < HEIGHT - 100: aleiny += 7

def draw():
    WIN.fill(CYAN)
    WIN.blit(image, (aleinx, aleiny))
    pygame.draw.rect(WIN, BLACK, border)
    pygame.draw.rect(WIN, BLACK, borderup)
    pygame.draw.rect(WIN, BLACK, borderleft)
    pygame.draw.rect(WIN, BLACK, borderright)
    pygame.display.flip()

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

if __name__ == '__main__':
    main()
