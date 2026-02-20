
from lab02_methods.tasks.thermometer import Thermometer

def test_thermometer():
    t = Thermometer(0)
    assert t.to_fahrenheit() == 32.0
