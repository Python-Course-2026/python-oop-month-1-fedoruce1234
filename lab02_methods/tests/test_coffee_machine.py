
from lab02_methods.tasks.coffee_machine import CoffeeMachine

def test_coffee_machine():
    m = CoffeeMachine(300, 10)
    assert m.make_coffee() == 'Error'
