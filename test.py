import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

dragging = False
object_x, object_y = 300, 200  # Initial position of the object

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            dragging = True
        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False

    if dragging:
        rel_x, rel_y = pygame.mouse.get_rel()
        object_x += rel_x
        object_y += rel_y

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (object_x, object_y, 50, 50))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()