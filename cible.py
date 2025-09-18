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

    def get_pos(self):
        return self.x, self.y
