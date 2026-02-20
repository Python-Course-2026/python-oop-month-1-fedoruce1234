from lab01_intro_classes.tasks.smartphone import Smartphone

def test_smartphone():
    s = Smartphone('Zen')
    s.use_app(120)
    assert s.battery == 0

