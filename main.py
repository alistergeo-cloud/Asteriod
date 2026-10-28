from logger import log_state
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
import pygame 

def main():
        print(f"Starting Asteroids with pygame version {pygame.version.ver}")
        print(f"""Screen width: {SCREEN_WIDTH}
        pygame.init()
Screen height: {SCREEN_HEIGHT}""")

while True: 
    log_state()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    
    # screen parameters and game windows
    Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Screen.fill("black")
    pygame.display.flip()

if __name__ == "__main__":
    main()
