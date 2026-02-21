
from lab01_intro_classes.tasks.circle import Circle

def test_circle():
    c = Circle(10)
    assert c.get_area() == 314.0

