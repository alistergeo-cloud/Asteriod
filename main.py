
from logger import log_state, log_event
from Player import Player
from shot import Shot
from Asteroid import Asteroid
from AsteroidField import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS
import pygame
import sys


def reset_game(updatable, drawable, asteroids, shots):
    # old stuff delete
    updatable.empty()
    drawable.empty()
    asteroids.empty()
    shots.empty()

    # Set up containers
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)

    # Create a new player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create a new asteroid field
    asteroid_field = AsteroidField()

    return player, asteroid_field

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    game_over = False

    # Fonts
    font = pygame.font.SysFont("dejavusamono", 50, bold=True)
    small_font = pygame.font.SysFont("dejavusamono", 20, bold=True)
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Shots
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    # Asteroid things
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    # Player things
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        screen.fill("black")

        # Only update game while playing
        if not game_over:

            for obj in updatable:
                obj.update(dt)

            for obj in drawable:
                obj.draw(screen)

            # Collision check for player
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    if player.invulnerability_timer <= 0:
                        player.lose_lives()
                        player.invulnerability_timer = 2
                        asteroid.split()

                        if player.get_lives() <= 0:
                            log_event("player_hit")
                            game_over = True

            # Collision check for shots
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collides_with(shot):
                        log_event("asteroid_shot")
                        asteroid.split()
                        shot.kill()

                        if asteroid.radius >= ASTEROID_MAX_RADIUS:
                            player.set_score(20)
                        elif asteroid.radius >= ASTEROID_MIN_RADIUS * 2:
                            player.set_score(50)
                        else:
                            player.set_score(100)

            # Display score and lives
            score_text = small_font.render(
                f"SCORE: {player.get_score()}", True, "white"
            )

            lives_text = small_font.render(
                f"LIVES: {player.get_lives()}", True, (0, 255, 100)
            )

            screen.blit(score_text, (20, 20))
            screen.blit(lives_text, (650, 20))

        else:
            # Game Over screen
            game_over_text = font.render("GAME OVER", True, "red")
            game_over_rect = game_over_text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
            )
            #score stuff
            score_text = small_font.render(
                f"SCORE: {player.get_score()}", True, "white"
            )
            score_rect = score_text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)
            )
            # restart text
            restart_text = small_font.render(
                "PRESS R TO RESTART", True, "white"
            )
            restart_rect = restart_text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)
            )
            screen.blit(game_over_text, game_over_rect)
            screen.blit(score_text, score_rect)
            screen.blit(restart_text, restart_rect)

        pygame.display.flip()
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player, asteroid_field = reset_game(
                        updatable, drawable, asteroids, shots
                    )
                    game_over = False
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("bye bye")
        pygame.quit()
        sys.exit()
