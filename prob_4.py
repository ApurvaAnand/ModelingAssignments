import math
visited=[]
top_list=[]#storing the topologically sorted list


input=open("frog2.txt","r") #reading the input file
lines=input.readlines()
no_of_lakes=lines[0][0]     #assigning the first line to be the number of lakes
x_coord=[]                  #storing x coordinates
y_coord=[]                  #storing y coordinates


	
for i in range(1,int(no_of_lakes)+1):
	x=lines[i][0]
	x_coord.append(x)
	y=lines[i][2]
	y_coord.append(y)
	

    #creating adjacency list for every node with its neighbors which satisfy the constrain

def adjacency():
	adj_list=dict()
	for i in range(0,len(x_coord)):
		for j in range(i+1,len(x_coord)):
			if i==j:
				continue
			x1=x_coord[i]
			x2=x_coord[j]
			
			y1=y_coord[i]
			y2=y_coord[j]
			
			x_last=x_coord[len(x_coord)-1]
			y_last=y_coord[len(y_coord)-1]
			
			x_ik=int(x1) - int(x_last)
			x_jk=int(x2) - int(x_last)
			
			x_ik_square=math.pow(x_ik,2)
			x_jk_square=math.pow(x_jk,2)
			
			y_ik=int(y1) - int(y_last)
			y_jk=int(y2) - int(y_last)
			
			y_ik_square=math.pow(y_ik,2)
			y_jk_square=math.pow(y_jk,2)
			
			lhs=x_ik_square + y_ik_square
			rhs=x_jk_square + y_jk_square
			
			if lhs>rhs:     #checking the constraint
				
			
				lake=i+1
				neighbor_lake=j+1
				
				if lake in adj_list:
					adj_list[lake].append(neighbor_lake)
				
				else:
					adj_list[lake]=[]
					adj_list[lake].append(neighbor_lake)

				adj_list[len(x_coord)]=[]
     
	return adj_list
	

 # this functions performs topological sort on the graph

def topological_sort(node):
	graph=adjacency()
	visited.append(node)

	for lake in graph[node]:
		if lake not in visited:
			topological_sort(lake)
	top_list.append(node)
	return top_list
	
# this function calculates the sum of probability of all the paths using dynamic programming	

def probability(node):
	order_top=topological_sort(node)
	
	t=int(no_of_lakes)
	prob_array={}    #initialising probability array which stores the probabilty of paths in going from 1 to t. This dictionary stores the probabilities of the paths for every vertes as key value pair
	prob_array[t]=1 #probability of going from vertex t which is the sink is to t=1
	graph=adjacency()
	
	for index in range(1,len(order_top)): #iterating over the nodes
		i=order_top[index]
		x_i=int(x_coord[i-1])
		y_i=int(y_coord[i-1])
		prob_array[i]=0
		
		for j in graph[i]:            #iterating over the neighbors of i
			x_j=int(x_coord[j-1])
			y_j=int(y_coord[j-1])
			distance=math.sqrt(math.pow((x_i-x_j),2)+math.pow((y_i-y_j),2))   #calculating distance ij
			prob_ij=math.pow((0.5),distance)                                  #calculating probability ij
			prob_ijt=(1.0/len(graph[i]))*prob_ij*prob_array[j]                #probabilty of path i-j-t=i/no. of neighbors * probability of path i to j * probability of path j to t
			prob_array[i]=prob_array[i]+prob_ijt     #probability of path i to t=probabilty of path i+probability of path i-j-t
			
	print prob_array[1]     #thevalue of the first key value pair=sum of probabilities of path from i to t
			

		
if __name__ == "__main__":
	root=1
	probability(root)


