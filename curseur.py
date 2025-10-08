import pygame

class Curseur:
    def __init__(self):
        self.x = 0
        self.y = 0

    def get_pos(self) -> tuple:
        return self.x, self.y

    def set_pos(self, pos: tuple) -> None:
        self.x = pos[0]
        self.y = pos[1]

    def move_pos(self, pos: tuple) -> None:
        self.x += pos[0]
        self.y += pos[1]

    def draw(self, screen : pygame.Surface) -> None:
        pygame.draw.circle(screen, "purple", self.get_pos(), 4, 2)
