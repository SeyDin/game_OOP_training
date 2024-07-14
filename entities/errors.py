class XPosException(Exception):

    def __int__(self, pos):
        self.pos = pos

    def __str__(self):
        return f"Invalid x position: {self.pos}"


class YPosException(Exception):

    def __int__(self, pos):
        self.pos = pos

    def __str__(self):
        return f"Invalid y position: {self.pos}"
