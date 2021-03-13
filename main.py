import pygame
import os




FPS = 60
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 1400, 800
VEL = 5
isJump = False
jumpCount = 10
walkCount = 0
left = False
right = False

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
TEMPLE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Temple_Time.jpeg')), (WIDTH, HEIGHT))

LINK_WIDTH, LINK_HEIGHT = 520, 330
LINK_IMAGE = pygame.image.load(os.path.join('Assets', 'Link_Standing.png'))
WalkLeft = pygame.image.load(os.path.join('Assets', 'Link_Face_Left.png'))
WalkRight = pygame.image.load(os.path.join('Assets', 'Link_Face_Right.png'))
LINK = pygame.transform.rotate(pygame.transform.scale(LINK_IMAGE, (LINK_WIDTH, LINK_HEIGHT)), 0) 
Link_Left = pygame.transform.rotate(pygame.transform.scale(WalkLeft, (LINK_WIDTH, LINK_HEIGHT)), 0) 
Link_Right = pygame.transform.rotate(pygame.transform.scale(WalkRight, (LINK_WIDTH, LINK_HEIGHT)), 0) 


def draw_surface(link, WalkLeft, WalkRight, left, right):
    #WIN.fill((WHITE))
    WIN.blit(TEMPLE, (0, 0))
    WIN.blit(LINK, (link.x, link.y))

    global walkCount
    
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        WIN.blit(Link_Left[walkCount//3], (link.x, link.y))
        walkCount += 1
    elif right:
        WIN.blit(Link_Right[walkCount//3], (link.x, link.y))
        walkCount += 1
    else: WIN.blit(LINK, (link.x, link.y))

    
    
    pygame.display.update() 



def link_movement(keys_pressed, link, jumpCount, isJump, left, right):
    if keys_pressed[pygame.K_a]:            #left
        link.x -= VEL
        left = True
        right = False
    elif keys_pressed[pygame.K_d]:                      #right
        link.x += VEL
        left = False
        right = True
    else:
        right = False
        left = False
        walkCount = 0
    
    if not(isJump):
        if keys_pressed[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= 10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    

         



def mainloop():
    link = pygame.Rect(60, 500, LINK_WIDTH, LINK_HEIGHT)                     
    
    clock = pygame.time.Clock()
    run = True                                 #The FIRST thing you always do when youre making a pygame, is write out this main function. 
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():       #The second thing you do, is check if the player has quit the game to end the loop with this function.
            if event.type == pygame.QUIT:
                run = False           
                pygame.quit()                                   #Without a main loop, python would not be able to draw the window, it would start and stop immediately. 

        
        keys_pressed = pygame.key.get_pressed()          #you must use this code to be able to press multiple keys at a time.
        link_movement(keys_pressed, link, isJump, jumpCount, left, right)
        draw_surface(link, WalkLeft, WalkRight, left, right)
        
        
       
    
          
        
        
if __name__ == "__main__":
    mainloop()                                
        
