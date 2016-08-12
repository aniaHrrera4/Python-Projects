import pygame
import random


from city2 import Scroller as Scroller

cornFlowerBlue=(100,149,237) 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
    return random.choice(colors)
	


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.



class Block(pygame.sprite.Sprite):
	def __init__ (self, color, width, height):
		super().__init__()
		
		
		#create an image of the block, and fill it with a color
		#this could also be an image from the disk
		self.image= pygame.Surface([width, height])
		self.image.fill(color)
		#xpos=random.randrange(0,700)
		#fetch the rectangle object that has the dimentions of the image
		#update the position of this object by setting the values of rect x and rect y 
		self.rect= self.image.get_rect()
		self.rect.x=SCREEN_WIDTH 
		
	def update(self)
		self.rect.x-=3
		if self.rect.x<0
			self.rect.y=random.randint(0,500)
			self.rect.x=710
		
	'''
	def __init__(self,size,pos):
	
		self.size=size
		self.pos=pos
	
	def movex(self, speed):
		self.pos[1]=self.pos[1]+speed
	'''
		
	
speed=1
pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Set the width and height of the screen [width, height]

greenBlock= pygame.sprite.Group()

allSprite= pygame.sprite.Group()

player=Block(BLACK,15,15)
Gblock=Block(GREEN,15,15)

def make_Blocks():
	allSprite.add(player)
	for i in range(50)
		greenBlock=Block(GREEN,15,15)
		Gblock.rect.x=710
		Gblock.rect.y=random.randint(0,500)


	
	
done = False


# Used to manage how fast the screen updates
clock = pygame.time.Clock()


FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 1)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 80), BACK_SCROLLER_COLOR, 3)


make_Blocks()

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
		elif event.type==pygame.KEYDOWN:
			make_Blocks()
						
	# --- Game logic should go here

	# --- Screen-clearing code goes here

	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.

	# If you want a background image, replace this clear with blit'ing the
	# background image.
	screen.fill(cornFlowerBlue)
	
	pos=pygame.mouse.get_pos()#returns (x,y) 
	player.rect.x=pos[0]
	player.rect.y=pos[1]
	# --- Drawing code should go here

	back_scroller.draw_buildings(screen)
	back_scroller.move_buildings()
	middle_scroller.draw_buildings(screen)
	middle_scroller.move_buildings()
	front_scroller.draw_buildings(screen)
	front_scroller.move_buildings()
	allSprite.draw(screen)
	greenBlock.draw(screen)

	#xpos=random.randrange(0,700)
	
	#greenBlock.append(Block(GREEN,[15,15], xpos,2))
	#blackBlock.apend(Block(BLACK, xpos))
	
	'''
	for block in greenBlock:
		block.draw()
		block.fall(speed)
	for block in blackBlock:
		block.draw()
		block.fall(speed)
	'''		
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
