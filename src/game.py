import pygame
from user_input import is_key_pressed, keys_down
from player import Player
from sprites import sprites



def start_game(running: bool, player):
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                keys_down.add(event.key)
            elif event.type == pygame.KEYUP:
                keys_down.remove(event.key)
    
        # update code

        player.update()
        
        # draw code 
        screen.fill(clear_color)
        for s in sprites:
            s.draw(screen)
        pygame.display.flip()
        pygame.time.delay(20)
    pygame.quit()



if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Adeventure Game")
    screen = pygame.display.set_mode((600,800))
    clear_color = (30, 120, 50)
    player = Player("images/test.png", 0 , 0)
    running = True
    start_game(running, player)