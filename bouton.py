import pygame

class Bouton:
    def __init__(self):
        self._action = None
        self._action_result = None
        self._x = 0
        self._y = 0
        self._text = ""
        self._hauteur = 0
        self._largeur = 0

    def draw(self):
        pass

    def action(self):
        self._action_result = self._action()

    def set_action(self, action):
        self._action = action