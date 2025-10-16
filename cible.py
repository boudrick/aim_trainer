import enum
import pygame


class Cible:
    class Modes(enum.Enum):
        FIXE = 0,
        SIZE = 1,
        AGE = 2

    DEFAUT_MAX_SIZE = 40#rayon px

    def __init__(self, x=0, y=0, rayon=DEFAUT_MAX_SIZE):
        self._mode = self.Modes.FIXE
        self._step = 0 # en %
        self._progression = 0 # en %
        self._x = x
        self._y = y
        self._rayon = rayon

    def set_pos(self, x, y):
        self._x = x
        self._y = y

    def get_pos(self):
        return self._x, self._y

    def move_pos(self, x, y):
        self._x += x
        self._y += y

    def draw(self, screen):
        rayon = self._rayon
        ratio = (1 - self.get_progress()) #1 -> 0

        if self._mode == self.Modes.SIZE:
            rayon *= ratio

        color = (int(255*(1-ratio)),int(255*ratio),0)

        pygame.draw.circle(screen, color, self.get_pos(), rayon)

    def set_mode(self, mode:Modes):
        self._mode = mode

    def get_mode(self):
        return self._mode

    def set_step(self, step=None, FPS=None, temps=None, pixel_s=None):
        if step is not None:
            self._step = step
            return
        if FPS is not None and temps is not None:
            self._step = 1/temps/FPS
            return
        if FPS is not None and pixel_s is not None:
            self._step = 1/FPS*pixel_s

    def progress(self) -> float:
        if self._mode != self.Modes.FIXE:
            self._progression += self._step

        if self._progression < 0:
            self._progression = 0
        elif self._progression > 1:
            self._progression = 1

        return self._progression

    def reset_progress(self):
        self._progression = 0

    def get_progress(self):
        return self._progression

    def set_progress(self, progress):
        self._progression = progress

    def get_step(self):
        return self._step

    def set_rayon(self, rayon):
        self._rayon = rayon

    def get_rayon(self):
        return self._rayon

    def mouse_on_cible(self, mouse_pos):
        on_cible = (self._rayon*(1 - self.get_progress()))**2 >= (self._x-mouse_pos[0])**2 + (self._y - mouse_pos[1])**2
        return on_cible