import pytest
import pygame
from Asteroid import Asteroid

#spawing
def test_asteroid_starts_at_correct_position():
    asteroid = Asteroid(100, 150, 20)
    assert asteroid.position.x == 100
    assert asteroid.position.y == 150

#radius
def test_asteroid_has_correct_radius():
    asteroid = Asteroid(100, 150, 20)
    assert asteroid.radius == 20