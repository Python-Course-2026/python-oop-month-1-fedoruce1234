
class Person:
    """Задача: person"""
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        """Возвращает True, если возраст 18+, иначе False"""
        return self.age >= 18

