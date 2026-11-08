from logger import log_state,log_event
from Player import Player
from shot import Shot
from Asteroid import Asteroid
from AsteroidField import AsteroidField
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,ASTEROID_MAX_RADIUS,ASTEROID_MIN_RADIUS
import pygame 
import sys 

def main():
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) 
        clock = pygame.time.Clock()
        dt = 0.0

        #Groups
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()

        #Shots
        shots = pygame.sprite.Group()
        Shot.containers = (shots, updatable, drawable)


        #Asteriod things
        asteroids = pygame.sprite.Group()
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable,)
        asteroid_field = AsteroidField()


        #player things
        Player.containers = (updatable, drawable)
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        #font
        font = pygame.font.SysFont("terminal", 25, bold=True)



        while True:
            screen.fill("black")
            #draw and update 
            for obj in updatable:
                obj.update(dt)
            for obj in drawable:
                obj.draw(screen)
            #collsion check for player
            for asteroid in asteroids:
                if asteroid.collides_with(player): 
                    if player.invulnerability_timer <= 0:
                        player.lose_lives()
                        asteroid.split()
                        if player.get_lives() <= 0:
                            log_event("player_hit")
                            print("Game over!")
                            sys.exit()
            #collsion check for shots     
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
            #text on screens
            player.draw(screen)
            score_text = font.render(
            f"SCORE: {player.get_score()}",
            True,
            (255, 255, 255)
            )
            lives_text = font.render(
            f"LIVES: {player.get_lives()}",
            True,
            (255, 255, 255)
            )

            screen.blit(lives_text, (650, 20))

            screen.blit(score_text, (20, 20))

            pygame.display.flip()
            log_state()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            # limit the framerate to 60 FPS
            dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
