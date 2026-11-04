from logger import log_state,log_event
from Player import Player
from shot import Shot
from Asteroid import Asteroid
from AsteroidField import AsteroidField
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
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


        while True:
        
            screen.fill("black")
            for obj in updatable:
                obj.update(dt)
            for obj in drawable:
                obj.draw(screen)
            for asteroid in asteroids:
                if asteroid.collides_with(player): 
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collides_with(shot):
                        log_event("asteroid_shot")
                        asteroid.split()
                        shot.kill()
            pygame.display.flip()
            
            log_state()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            # limit the framerate to 60 FPS
            dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
