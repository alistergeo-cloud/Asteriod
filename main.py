from logger import log_state
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
import pygame 

def main():
        pygame.init
        Screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) 
        pygame.display.flip()
        while True: 
            Screen.fill("black")
            log_state()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            pygame.display.flip

if __name__ == "__main__":
    main()
