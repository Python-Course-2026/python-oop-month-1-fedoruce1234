

from lab04_simple_projects.tasks.zoo import Zoo

def test_zoo():
    z = Zoo()
    z.add('Lion')
    assert len(z.animals) == 1
