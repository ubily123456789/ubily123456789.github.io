# just learning pygame
import pygame
import os

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my game!")

FPS = 60
VEL = 5
SHIP_WIDTH, SHIP_HEIGHT = 55, 40

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 0, 255)

YELLOW_SHIP = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SHIP, (SHIP_WIDTH, SHIP_HEIGHT)), 90)
RED_SHIP = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SHIP = pygame.transform.rotate(pygame.transform.scale(RED_SHIP, (SHIP_WIDTH, SHIP_HEIGHT)), 270)

def draw_window(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SHIP, (red.x, red.y))
    pygame.display.update()

def main():
    red = pygame.Rect(700, 300, SHIP_WIDTH, SHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SHIP_WIDTH, SHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(red, yellow)
        keys_press = pygame.key.get_pressed()
        if keys_press[pygame.K_a]: # Left
            yellow.x -= VEL
        if keys_press[pygame.K_d]: # Right
            yellow.x += VEL
        if keys_press[pygame.K_w]: # Up
            yellow.y -= VEL
        if keys_press[pygame.K_s]: # Down
            yellow.y += VEL
        if keys_press[pygame.K_LEFT]: # Left
            red.x -= VEL
        if keys_press[pygame.K_RIGHT]: # Right
            red.x += VEL
        if keys_press[pygame.K_UP]: # Up
            red.y -= VEL
        if keys_press[pygame.K_DOWN]: # Down
            red.y += VEL
    pygame.quit()

if __name__ == "__main__":
    main()
