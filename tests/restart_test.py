
import pygame
import pytest
import main

@pytest.fixture
def game_groups():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    return updatable, drawable, asteroids, shots

    
def test_reset_clears_groups(game_groups):
    updatable, drawable, asteroids, shots = game_groups

    # example sprite
    sprite = pygame.sprite.Sprite()

    updatable.add(sprite)
    drawable.add(sprite)
    asteroids.add(sprite)
    shots.add(sprite)

    # Reset the game
    main.reset_game(updatable, drawable, asteroids, shots)

    # Check the old sprite was removed
    assert sprite not in updatable
    assert sprite not in drawable
    assert sprite not in asteroids
    assert sprite not in shots