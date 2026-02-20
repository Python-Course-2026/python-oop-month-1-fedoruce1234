from lab01_intro_classes.tasks.dog import Dog

def test_dog():
    d = Dog('Rex')
    assert d.bark() == 'Woof!'

