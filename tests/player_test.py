from Player import Player

def test_player_starts_with_zero_rotation():
    player = Player(100, 100)
    assert player.rotation == 0

def test_player_starts_at_correct_position():
    player = Player(100, 150)
    assert player.position.x == 100
    assert player.position.y == 150