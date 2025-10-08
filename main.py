import random
from enum import Enum

import pygame

from cible import Cible
from curseur import Curseur


class Modes(Enum):
    STANDARD = 0
    SPHERE = 1
    PERSPECTIVE = 2

#CONST
H_WIDTH, H_HEIGHT = 800, 600
TARGET_MAX = 3
FPS = 120
SENS = 1
MODE = Modes.SPHERE
REDUCTION = 5/FPS #pixel/s

# pygame setup
pygame.init()
screen = pygame.display.set_mode((H_WIDTH, H_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
curseur = Curseur()
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

liste_cibles = []

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:# main loop
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    mouse_pos = pygame.mouse.get_pos()


    #traitement
    if pygame.mouse.get_pressed()[0]: #click sur cible
        for cible in liste_cibles:
            if cible.mouse_on_cible(mouse_pos):
                liste_cibles.remove(cible)

    for cible in liste_cibles:
        cible.size -= REDUCTION
        if cible.size <= 0:
            liste_cibles.remove(cible)

    if MODE == Modes.SPHERE:
        relatif = pygame.mouse.get_rel()
        pygame.mouse.set_pos(H_WIDTH/2, H_HEIGHT/2)
        _ = pygame.mouse.get_pos()
        curseur.set_pos(pygame.mouse.get_pos())
        for cible in liste_cibles:
            cible.move_pos(relatif)

    if MODE == Modes.STANDARD:
        curseur.set_pos(pygame.mouse.get_pos())


    if len(liste_cibles) < TARGET_MAX: #gestion du nombre de cible
        x = random.randint(0,H_WIDTH)
        y = random.randint(0,H_HEIGHT)
        liste_cibles.append(Cible(x,y))

    #affichage
    screen.fill("black")

    for cible in liste_cibles:
        cible.draw(screen)

    curseur.draw(screen)

    pygame.display.flip()

    dt = clock.tick(FPS)

pygame.quit()
