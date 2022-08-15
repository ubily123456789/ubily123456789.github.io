import pygame

def highscore():
    pygame.font.init()
    background_colour = (255,255,255)
    (width, height) = (600, 600)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tutorial 1')
    screen.fill(background_colour)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        myfont = pygame.font.SysFont("monospace", 75)
        BLACK = (0, 0, 0)
        label = myfont.render("Tutorial 1", 1, BLACK)
        screen.blit(label, (0, 10))
        pygame.display.update()

highscore()
