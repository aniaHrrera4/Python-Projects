"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
rosyBrown=(188,143,143)
mediumPurple=(147,112,219)
skyBlue=(135,206,235)
teal=(0,128,128)
mediumSeaGreen=(60,179,113)
salmon=(250,128,114) 
maroon=(128,0,0) 
cornFlowerBlue=(100,149,237) 
darkOrchid=(153,50,204) 


pygame.init()

snow_list=[]

pos=()
x=10
y=10
pos=x,y
radius=10
width=0
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")
y_speed=1
x_speed=-1

class SnowFlake():
	'''
	This class will be used to create the SnowFlake Objects.
    It takes: 
		size - an integer that tells us how big we want the snowflake
		position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
		wind - a boolean that lets us know if there is any wind or not.  
	'''
	#pointlist=[(x,y+6),(),(),(),(),(),]
	def __init__(self, size, position, wind=False):
		self.size=size 
		self.position=position
		self.wind=wind
    
	def fall(self, x_speed,y_speed):
		"""
		Take in a integer that represnts the speed at which the snowflake is falling in the y-direction.  
		A positive integer will have the snowflake falling down the screen. 
		A negative integer will have the snowflake falling up the screen. 
		If wind = True
		- the x direction of the snowflake changes
		"""

		
		#fall=True
		'''
		if fall==True :
			if event.type==pygame.MOUSEBUTTONDOWN:
				pos=pygame.mouse.get_pos()#returns (x,y) 
				y=y+10
		'''
		wind=True
		if wind==True: 
			self.position[0]=self.position[0]+x_speed
			self.position[1]=self.position[1]+y_speed
				
					
	def draw(self,screen,snowcolor,pos,radius,width):
		self.screen=screen
		self.snowcolor=snowcolor
		self.pos=pos
		self.radius=radius
		self.width=width
		pygame.draw.circle(screen, snowcolor, pos,radius,width)
		"""
		Uses pygame and the global screen variable to draw the snowflake on the screen
		"""
        

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# Speed
speed = 1


#INITIALIZE YOUR SNOWFLAKE HERE! 

# Snow List
snow_list =[]

# -------- Main Program Loop -----------
while not done:
	colors=[maroon,rosyBrown,mediumPurple,skyBlue,teal,salmon,cornFlowerBlue,darkOrchid,WHITE]
	snowcolor = random.choice(colors) 
# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
	screen.fill(BLACK)

    # --- Drawing code should go here

	snow=SnowFlake(size,pos,)
	snow.draw(screen, snowcolor,(x,y),radius,width)	
	snow.draw(screen, snowcolor,(30,y),radius,width)	
	snow.draw(screen, snowcolor,(70,y),radius,width)	
	snow.draw(screen, snowcolor,(110,y),radius,width)	
	snow.draw(screen, snowcolor,(150,y),radius,width)
	snow.fall(x_speed, y_speed)
	
    # Begin Snow

    


    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

    # --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
