import pygame
import os


FPS = 60
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 1400, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
TEMPLE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Temple_Time.jpeg')), (WIDTH, HEIGHT))

LINK_WIDTH, LINK_HEIGHT = 600, 300
LINK_IMAGE = pygame.image.load(os.path.join('Assets', 'Link_Face_Right.png'))
LINK = pygame.transform.rotate(pygame.transform.scale(LINK_IMAGE, (LINK_WIDTH, LINK_HEIGHT)), 0) 


def draw_surface():
    WIN.fill((WHITE))
    WIN.blit(TEMPLE, (0, 0))
    WIN.blit(LINK, (60, 500))
    pygame.display.update()
    


def mainloop():                     
    
    clock = pygame.time.Clock()
    run = True                                 #The FIRST thing you always do when youre making a pygame, is write out this main function. 
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():       #The second thing you do, is check if the player has quit the game to end the loop with this function.
            if event.type == pygame.QUIT:
                run = False           
                pygame.quit()                                   #Without a main loop, python would not be able to draw the window, it would start and stop immediately. 

        
        draw_surface()
        
        


if __name__ == "__main__":
    mainloop()                                
        
