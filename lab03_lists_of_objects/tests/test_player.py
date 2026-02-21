

from lab03_lists_of_objects.tasks.player import Player

def test_player():
    p = Player('Ace')
    p.add_score(10)
    assert p.score == 10

