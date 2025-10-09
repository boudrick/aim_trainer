import pygame

class Curseur:
    SIZE = 20
    COLOR = "purple"
    RADIUS = 1
    COLOR_KEY = "black"

    def __init__(self):
        self.x = 0
        self.y = 0
        self.surface_curseur = None
        self._dessine_curseur()

    def get_pos(self) -> tuple:
        return self.x, self.y

    def set_pos(self, pos: tuple) -> None:
        self.x = pos[0]
        self.y = pos[1]

    def move_pos(self, pos: tuple) -> None:
        self.x += pos[0]
        self.y += pos[1]

    def draw(self, screen : pygame.Surface) -> None:
        x = self.x - self.surface_curseur.get_width()/2
        y = self.y - self.surface_curseur.get_height()/2
        screen.blit(self.surface_curseur, (x, y))

    def _dessine_curseur(self):
        self.surface_curseur = pygame.Surface([self.SIZE, self.SIZE])
        self.surface_curseur.fill(self.COLOR_KEY)
        self.surface_curseur.set_colorkey(self.COLOR_KEY)
        pygame.draw.rect(self.surface_curseur, self.COLOR, pygame.Rect(self.SIZE/2 - self.RADIUS, 0, self.RADIUS*2, self.SIZE)) #vertical
        pygame.draw.rect(self.surface_curseur, self.COLOR, pygame.Rect(0, self.SIZE/2 - self.RADIUS, self.SIZE, self.RADIUS*2)) #horizontal
        pygame.draw.rect(self.surface_curseur, self.COLOR_KEY, pygame.Rect(self.SIZE/2 - self.RADIUS*3, self.SIZE/2 - self.RADIUS*3, self.RADIUS*6, self.RADIUS*6))  # centre
        pygame.draw.circle(self.surface_curseur, self.COLOR, (self.SIZE/2, self.SIZE/2), self.RADIUS) # centre
