

from lab03_lists_of_objects.tasks.team import Team

def test_team():
    t = Team('Devs')
    t.join('Alice')
    assert 'Alice' in t.members
