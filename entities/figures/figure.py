from abc import ABC

from entities.errors import XPosException, YPosException
from entities.looks.square_look import SquareLook


class Figure(ABC):

    def __init__(self, x: int, y: int, look: SquareLook):
        self._x = x
        self._y = y
        self.look = look

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x):
        if x < 0 or x > self.look.screen.get_width() - self.look.x_size:
            raise XPosException("X out of range")
        self._x = x

    @y.setter
    def y(self, y):
        if y < 0 or y > self.look.screen.get_height() - self.look.y_size:
            raise YPosException("Y out of range")
        self._y = y

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def change_position(self, x: int = 0, y: int = 0, position: tuple[int, int] = None):
        if x or y:
            if x:
                self.x = x
            else:
                self.y = y
        elif position:
            self.x = position[0]
            self.y = position[1]
        elif (x or y) and position:
            raise ValueError("You can't use both x and y and position")
        self.x = x
        self.y = y

    def draw(self, x: int = None, y: int = None, position: tuple[int, int] = None, dx: int = 0, dy: int = 0):
        if x and y:
            self.change_position(x, y)
        elif position:
            self.change_position(position[0], position[1])
        elif (x or y) and position:
            raise ValueError("You can't use both x and y and position")
        if dx or dy:
            self.move(dx, dy)
        self._draw()

    def _draw(self):
        pass
