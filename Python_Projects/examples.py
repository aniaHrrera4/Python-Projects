'''
for i in range(5):
	print("inside for")
	print(i)
print("end of for loop ")



for a in range(3):
	print("hi")
	for b in range(2):


def greet(name,color):
	print("name:"+ name+ " favorite color:"+ color)
	
greet("andrea","blue")
greet("erika","purple")
greet("denise","aqua") 

from turtle import *

def drawsquare(color):
	setcolor=color 
	for i in range(4):
		pendown()
		forward(100)
		turn(90)

drawsquare("black")
drawsquare("pink") 



#color=(1,2,3)   #tuple (uses parenthesis)
#print(color[0])  

# color[1]=4  << will get u an error because tupls cannot be edited 

color=[1,2.5,"hello"]
color[1]=4
print(color[1])


color.append(5) 
print(color)

color.insert(1,10)
print(color)

color.pop(2) 
print(color)
'''

my_list=[(0,1,2),[1,5,2],"hello"]

print(my_list[1]) #0,1,2
print(my_list[0][2]) #1
print(my_list[2][3]) #L