class Entity:
    """
    A generic object to represent, player, items, enemies, etc.
    """

    def __init__(self, x, y, char, color): # datos para el hijo
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

