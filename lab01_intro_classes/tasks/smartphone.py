
class Smartphone:
    """Задача: smartphone"""
    def __init__(self, model: str):
        self.model = model
        self.battery = 100

    def use_app(self, cost: int):
        """Снижает заряд, но не ниже 0"""
        self.battery = max(0, self.battery - cost)
