

from lab02_methods.tasks.robot import Robot

def test_robot():
    r = Robot()
    r.move_forward()
    r.move_right()
    assert (r.x, r.y) == (1, 1)

