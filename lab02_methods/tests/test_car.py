

from lab02_methods.tasks.car import Car

def test_car():
    c = Car()
    c.accelerate(50)
    c.brake(100)
    assert c.speed == 0

