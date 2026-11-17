import pygame
import pytest

pygame.init()
pygame.mixer.init()

from Player import Player
# without this pytest trows up error "mixer not intialsied"
def test_player_without_mixer():
    pygame.mixer.quit()

    with pytest.raises(pygame.error, match="mixer not initialized"):
        Player(100, 100)

    pygame.mixer.init()

#   rotation
def test_player_starts_with_zero_rotation():
    player = Player(100, 100)
    assert player.rotation == 0
#   postion
def test_player_starts_at_correct_position():
    player = Player(100, 150)
    assert player.position.x == 100
    assert player.position.y == 150