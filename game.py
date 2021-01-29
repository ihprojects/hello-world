import pygame
pygame.init()
#create window
screen = pygame.display.set_mode((800,500))

##
# TODO: create class for constant values

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
    
    pygame.display.update()       #refresh window


pygame.quit()  # If we exit the loop this will execute and close our game