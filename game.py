import pygame
import gameobjects

pygame.init()
#create window
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))

#Settings
bg_color = (0,0,0)      #backgound color

##
player1 = gameobjects.Player(20,300,50,80,screen)           #create player object
testblock = gameobjects.Block(0,screen_height-50, screen_width-200,50,screen)   #create block object


blocks = [testblock]        #list of blocks in this level
clock =pygame.time.Clock()
run = True
while run:
    clock.tick(60)
    #pygame.time.delay(100) # This will delay the game the given amount of 
    # milliseconds. In our casee 0.1 seconds will be the delay
    # 
    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        player1.right = True
    if keys[pygame.K_a]:
        player1.left = True
    if keys[pygame.K_w]:
        player1.jump = True
    player1.move(blocks)

    screen.fill(bg_color)         #clear window
    player1.draw()
    testblock.draw()
    pygame.display.update()       #refresh window


pygame.quit()  # If we exit the loop this will execute and close our game