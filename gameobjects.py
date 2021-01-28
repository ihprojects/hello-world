import pygame
def collision_check( player, block ):
    if player.y + player.height > block.y:
        player.y = block.y - player.height
        player.is_in_air = False    

class Player(object):
    def __init__(self,x,y,width, height,win):
        self.x = x          #x position
        self.y = y          #y position
        self.width = width
        self.height = height
        self.move_speed = 10       #movement speed
        self.jumpspeed = -15
        self.jump =False
        self.is_in_air =True
        #self.hitbox = (self.x, self.y, 28,60)
        self.win = win      #window we want to draw on
        self.gravity = 1     #how much this player is affected by gravity
        self.vert_vel = 5     #vertical velocity
        # self.up =False      
        # self.down = False
        self.right = False
        self.left = False

    def draw(self):
        pygame.draw.rect(self.win, (255,0,0), (self.x,self.y,self.width,self.height),5)

    def move(self, blocks):
        if self.right:
            self.x += self.move_speed
            self.right = False
        if self.left:
            self.x -= self.move_speed
            self.left = False
        
        if self.is_in_air:
            self.vert_vel += self.gravity
            self.jump =False
        else:
            if self.jump:
                self.vert_vel = self.jumpspeed
                self.is_in_air = True
        self.y += self.vert_vel
        for i in blocks:
            collision_check(self, i)
        
class Block():
    def __init__(self,x,y,width, height,win):
        self.x = x          #x position
        self.y = y          #y position
        self.width = width
        self.height = height
        self.win = win      #window we want to draw 
    def draw(self):
        pygame.draw.rect(self.win, (25,120,14), (self.x,self.y,self.width,self.height))


