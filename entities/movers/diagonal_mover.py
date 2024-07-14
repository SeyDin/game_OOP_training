from entities.errors import XPosException, YPosException
from entities.figures.figure import Figure


class DiagonalMover:
    def __init__(self, figure: Figure, dx: int = 2, dy: int = 2):
        self.figure = figure
        self.dx = dx
        self.dy = dy

    def move(self):
        try:
            self.figure.move(self.dx, self.dy)
        except XPosException:
            self.dx = -self.dx
        except YPosException:
            self.dy = -self.dy
        self.figure.draw()
