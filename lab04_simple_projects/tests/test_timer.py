
from lab04_simple_projects.tasks.timer import Timer

def test_timer():
    t = Timer(1)
    t.tick()
    t.tick()
    assert t.sec == 0
