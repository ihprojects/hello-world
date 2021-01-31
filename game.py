import pygame

def draw_lines(display_surface, availabe_width, available_height):
    margin = 2
    
    if availabe_width < (available_height - 50) :
        max_field_length = available_width
    else:
        max_field_length = available_height - 50 # remove text height
    
    # leeve margin
    max_field_length -= margin*2
    from_x = margin
    to_x = max_field_length - margin*2
    from_y = 50 + margin
    to_y = max_field_length - margin*2 + 50 # add text hight for correct y possition
    
    step = (max_field_length - margin*2) // 10
    curr_x = from_x
    curr_y = from_y
    for i in range(1, 12): # need to draw 12 lines
        pygame.draw.line(display_surface, gray, (from_x, curr_y), (to_x, curr_y), 2) # horizontal line - y is changing
        print(f"horizontal ({from_x},{curr_y}), ({to_x},{curr_y})")
        pygame.draw.line(display_surface, gray, (curr_x, from_y), (curr_x, to_y), 2) # vertical line - x is changing
        print(f"vertical ({curr_x},{from_y}), ({curr_x},{to_y})")
        curr_x += step
        curr_y += step

# '            for i in range(50, 450, 100):
#                 pygame.draw.line(gameDisplay, gray, (i, 50), (i, 350), 2)
#             pygame.draw.line(gameDisplay, gray, (50, i), (350, i), 2)'

word_1 ={
    'english_word':'chair',          # Der zu übersetzende englische Begriff
    'german_choose_word':['Tisch','Stuhl','Sessel'],    # Liste der möglichen Antworten
    'answer_index':2,               # Nummer der richtigen Antwort in Listenelement
    'is_learned':False,          # Wurde richtig geantwortet TRUE / FALSE
    'trained_at':'',            # datetime.datetime(2021, 1, 27), todo ??? Type Datum und Zeit der Beantwortung
    }
print(f"Wie heißt das Wort '{word_1['english_word']}' auf Deutsch?")

white = (255, 255, 255)
black = (0,0,0)
gray = (0, 0, 0)
green = (0, 255, 128)
red = (255, 64, 64)

width = 800
height = 600

pygame.init()

# create the display surface object
display_surface = pygame.display.set_mode((width, height))

pygame.display.set_caption('Vokabulary')

display_surface.fill(white)
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 30)

msg_question = f"Wie heißt das Wort '{word_1['english_word']}' auf Deutsch?"

# create a text suface object,
# on which text is drawn on it.
text = font.render(msg_question, True, black)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
#textRect.center = (X // 2, Y // 2)
textRect.center = (height // 2, 25)

# copying the text surface object
# to the display surface object
# at the center coordinate.
display_surface.blit(text,textRect)

draw_lines(display_surface, width, height)
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