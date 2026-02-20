class Student:
    """Задача: student_grades"""
    def __init__(self, name: str):
        self.grades = []

    def add_grade(self, g: int):
        pass

    def average(self) -> float:
        return sum(self.grades) / len(self.grades)

