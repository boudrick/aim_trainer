# Example file showing a circle moving on screen
import pygame

#CONST
H_WIDTH, H_HEIGHT = 800, 600
TARGET_MAX = 1

# pygame setup
pygame.init()
screen = pygame.display.set_mode((H_WIDTH, H_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

target_display = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running: # main loop

    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()


    #traitement
    if target_display < TARGET_MAX:
        



    #affichage
    screen.fill("black")

    pygame.draw.circle(screen, "red", mouse_pos, 40, 3)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
