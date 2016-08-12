from turtle import *

def drawSquare(color,sideLength):
	pencolor(color) 
	for i in range(4):
		pendown()
		forward(sideLength)
		right(90)
		
	penup()
	forward(60)

drawSquare("black",50)
drawSquare("blue",50)
drawSquare("red",50) 
clear()
goto(0,0)

def drawTri(color,sideLength): 
	pencolor(color)
	for i in range(3):
		pendown()
		forward(sideLength)
		right(120)
	penup()
	forward(100)		
		
drawTri("green",100)
clear()
goto(0,0)

def drawPoly(color,sideLength,angle,sides):
	pencolor(color) 
	for i in range(sides):
		pendown()
		forward(sideLength)
		right(angle) 
	penup()
	forward(120)		
	

drawPoly("purple",100,60,6)  
clear()
goto(0,0)	


def drawComplexPoly(color,sideLength,angle,sides):
	
	for a in range(1):
		pencolor(color)
		for i in range(sides):
			speed(5)
			pendown()
			forward(sideLength)
			right(angle) 
		forward(4) 
		  
for c in range(100):

	drawComplexPoly("blue",50,60,6) 
	drawComplexPoly("red",50,60,6) 
	drawComplexPoly("black",50,60,6)  


			



