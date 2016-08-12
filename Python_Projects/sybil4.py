  #graph code 3

from igraph import * #importing igraph from library 

g=Graph(3) # number of nodes 

g.add_edge(0,1)
g.add_edge(0,2)


for i in range(0,g.vcount()): # g.vcount() counts 
	print(g.degree(i))

summary(g) #print information about the g 

plot(g, "code1.pdf")  
