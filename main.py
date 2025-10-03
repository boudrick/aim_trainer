import random

import pygame

from cible import Cible

#CONST
H_WIDTH, H_HEIGHT = 800, 600
TARGET_MAX = 3

# pygame setup
pygame.init()
screen = pygame.display.set_mode((H_WIDTH, H_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

liste_cibles = []

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running: # main loop

    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()


    #traitement
    if pygame.mouse.get_pressed()[0]:
        for cible in liste_cibles:
            if cible.mouse_on_cible(mouse_pos):
                liste_cibles.remove(cible)

    if len(liste_cibles) < TARGET_MAX:
        x = random.randint(0,H_WIDTH)
        y = random.randint(0,H_HEIGHT)
        liste_cibles.append(Cible(x,y))
        



    #affichage
    screen.fill("black")

    for cible in liste_cibles:
        cible.draw(screen)

    pygame.draw.circle(screen, "red", mouse_pos, 40, 3)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
