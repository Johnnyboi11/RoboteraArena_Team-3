import pygame
import random

# initialize game
pygame.init()

# determine the screen display size for the game
screen = pygame.display.set_mode((1280,720))


# coordinates on the screen: (300,250), Width/Height of player Rectangle: (150,150)
player = pygame.Rect(300,250, 150,150)

# Parameters for Food spawning
eaten = True

foodX= random.randrange(1280)

foodY = random.randrange(720)

while True:
    

    # Refresh screen at the start of each loop
    screen.fill('black')
    # Draw red player rectangle
    pygame.draw.rect(screen, (255, 0, 0), player)
    
    #if the food was eaten, the Coordinates will change
    if(eaten):  
        foodX= random.randrange(1280)

        foodY = random.randrange(720)
        eaten = False

    #draw the food
    food = pygame.Rect(foodX,foodY, 15,15)      
    pygame.draw.rect(screen,"yellow", food)    
       
    #if collision occurs, the food will be eaten
    if(player.colliderect(food)):
        eaten=True

    
    

    key = pygame.key.get_pressed()

    # Process player inputs - WASD
    if key[pygame.K_a] == True:
        # moving left
        player.move_ip(-1, 0)    # move_ip = "move in place"
    elif key[pygame.K_d] == True:
        # moving right
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        # moving up
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        # moving down
        player.move_ip(0, 1) 
        
    # Event-loop for quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Refresh on-screen display
    pygame.display.flip()  # Refresh on-screen display