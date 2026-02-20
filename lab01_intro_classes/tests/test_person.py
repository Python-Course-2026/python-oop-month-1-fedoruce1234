from lab01_intro_classes.tasks.person import Person

def test_person():
    p = Person('Ivan', 20)
    assert p.is_adult() is True
    assert Person('Kim', 15).is_adult() is False

