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
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
lightSeaGreen=(32,178,170)
rosyBrown=(188,143,143)
mediumPurple=(147,112,219)
skyBlue=(135,206,235)
teal=(0,128,128)
mediumSeaGreen=(60,179,113)
mediumAquaMarine=(102,205,170)
salmon=(250,128,114) 
golden=(218,165,32) 
maroon=(128,0,0) 
darkTurquoise=(0,206,209) 
cornFlowerBlue=(100,149,237) 
darkOrchid=(153,50,204) 




pygame.init()




# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


possible_ball_colors = [BLACK, WHITE, GREEN, RED, BLUE, GREY,lightSeaGreen,rosyBrown,mediumPurple,skyBlue,teal,mediumAquaMarine,mediumSeaGreen,salmon,golden,maroon,darkOrchid,darkTurquoise,cornFlowerBlue]



x_speed = random.randint(-10, 10)
y_speed = random.randint(-10, 10)

x_loc= int(SCREEN_WIDTH/2)
y_loc= int(SCREEN_HEIGHT/2)


ball_size =random.randint(20,80)


# -------- Main Program Loop -----------
while not done:
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
    screen.fill(teal)

    # --- Drawing code should go here

    ball_color = random.choice(possible_ball_colors) # This is outside because of variable scoping.


    pygame.draw.circle(screen, ball_color, [x_loc, y_loc], ball_size)


    if x_loc>= SCREEN_WIDTH - ball_size or x_loc< ball_size:
        x_speed = x_speed * -1

    if y_loc>= SCREEN_HEIGHT - ball_size or y_loc< ball_size:
        y_speed = y_speed * -1


    x_loc += x_speed
    y_loc+= y_speed




    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
