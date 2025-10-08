import pygame


class Cible:
    DEFAUT_MAX_SIZE = 40#rayon px

    def __init__(self, x=None, y=None, pos=(0,0), size_max=DEFAUT_MAX_SIZE):
        self.x = x
        self.y = y
        if x is None and y is None:
            self._set_pos(pos)
        self.size_max = size_max
        self.size = self.size_max

    def _set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def get_pos(self):
        return self.x, self.y

    def move_pos(self, relatif):
        self.x += relatif[0]
        self.y += relatif[1]

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.get_pos(), self.size)

    def mouse_on_cible(self, mouse_pos):
        on_cible = self.size**2 >= (self.x-mouse_pos[0])**2 + (self.y - mouse_pos[1])**2
        return on_cible