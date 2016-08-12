  #graph code 2

from igraph import * #importing igraph from library 

g=Graph(3) # number of nodes 

for i in range(0,g.vcount()): #g.vcount() counts 
	print(g.degree(i))

summary(g) #print information about the g 

plot(g, "code2.pdf")  
