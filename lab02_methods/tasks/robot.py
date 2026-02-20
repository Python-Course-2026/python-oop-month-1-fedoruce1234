class Robot:
    """Задача: robot"""
    def __init__(self):
        self.x, self.y = 0, 0

    def move_forward(self):
        self.y += 1

    def move_right(self):
        self.x += 1

