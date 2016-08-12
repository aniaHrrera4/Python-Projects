start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maze.
A sign is hanging from the ivy: “You have one hour. Don’t touch the walls.”
There is a hallway to your right and to your left.
'''


print(start)

print("Type 'left' to go left or 'right' to go right.")
user_input = input()
done=False
while done==False:
	if user_input == "left":
		print("You decide to go left and come across a bridge. you cross the bridge and continue along until u come to a mysterioiu door.") # finished the story by writing what happens
		door=input("do you choose to open or close?:")
		if door=="open":
			print("you open the door and find a slide, you notice that it leads to an exit so you decide to take it and exit the maze")
			done = True
		else: 
			print("you continue on your journey and evetually get lost")
			done=True
	elif user_input == "right":
		print("You choose to go right and encounter a hydra. you feel threatened you can decide to slay the hydra or let it live ") # finished the story writing what happens
		hydra=input("do you want to slay or let it live?: ")
		if hydra=="slay":
			print("you killed a friendly hydra that only wanted to help you get ou of the maze. now you are lost")
			done=True
		else:
			print("the hydra realizes you are lost and wants to help you get out he  gives you directions, to find a way out.")
			done = True
