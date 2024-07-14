from abc import ABC


class Accelerator(ABC):

    def inc_speed(self):
        """increment the speed"""

    def dec_speed(self):
        """decrement the speed"""

    def get_dx(self):
        """get the x-axis acceleration"""

    def get_dy(self):
        """get the y-axis acceleration"""

