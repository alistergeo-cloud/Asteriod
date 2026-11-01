from logger import log_state
from Player import Player
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
import pygame 

def main():
        pygame.init
        screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) 
        clock = pygame.time.Clock()
        dt = 0.0
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        Player.containers = (updatable, drawable)
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        while True:
        
            screen.fill("black")
            updatable.update(dt)
            for obj in drawable:
                obj.draw(screen)
            pygame.display.flip()
            
            log_state()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            # limit the framerate to 60 FPS
            dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
