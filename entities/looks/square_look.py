from dataclasses import dataclass

from pygame import Surface


@dataclass
class SquareLook:
    x_size: int
    color: tuple
    screen: Surface

    @property
    def y_size(self):
        return self.x_size
