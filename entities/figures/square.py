import pygame

from entities.figures.figure import Figure
from entities.looks.square_look import SquareLook


class Square(Figure):

    def __init__(self, x: int, y: int, look: SquareLook):
        super().__init__(x, y, look)

    def _draw(self):
        pygame.draw.rect(
            self.look.screen,
            self.look.color,
            pygame.Rect(self.x, self.y, self.look.x_size, self.look.y_size)
        )


