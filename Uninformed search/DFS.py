
'''
Travel to Romania - Adjacency matrix

	arad	zerand	oradea	sibiu	fagaras	 timisora  lugoj  mehadia  dobreta  craiova pitesti rimmi bucharest  
arad	  0       1       0       1       0         1         0     0         0       0         0      0     0
zerand	  1       0       1       0       0         0         0     0         0       0         0      0     0
oradea	  0       1       0       1       0         0         0     0         0       0         0      0     0
sibiu	  1       0       1       0       1         0         0     0         0       0         0      1     0
fagaras   0       0       0       1       0         0         0     0         0       0         0      0     1
timisora  1       0       0       0       0         0         1     0         0       0         0      0     0
lugoj     0       0       0       0       0         1         0     1         0       0         0      0     0
mehadia   0       0       0       0       0         0         1     0         1       0         0      0     0
dobreta   0       0       0       0       0         0         0     1         0       1         0      0     0
craiova   0       0       0       0       0         0         0     0         1       0         1      1     0
pitesti   0       0       0       0       0         0         0     0         0       1         0      1     1
rimmi     0       0       0       1       0         0         0     0         0       1         1      0     0
bucharest 0       0       0       0       1         0         0     0         0       0         1      0     0

'''


graph=[
    [0,1,0,1,0,1,0,0,0,0,0,0,0],
    [1,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,0,1,0,0,0,0,0,0,0],
    [1,0,1,0,1,0,0,0,0,0,0,1,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,1,0,1,1],
    [0,0,0,1,0,0,0,0,0,1,1,0,0],
    [0,0,0,0,1,0,0,0,0,0,1,0,0]
]

stack = []


def DepthFirstSearch(graph,start,goal):
    stack = []
    visited_nodes=set([])
    way=[]
    state=start
    stack.append(state)
    while state!=goal:
        print(stack)
        # the last node stacked is the one who is going to be branched
        state=stack.pop()
        # the way array is used to save the way taken throughout the algorithm execution
        way.append(state)

        # Look for the neighbors of the current state
        for j in range(len(graph[state])):
            #print(graph[state][j],end=" ")

            
            if(graph[state][j]==1 and j not in visited_nodes):
                # those neighbors who were no visited before are added to the visited_nodes set and are pushed into the stack
                visited_nodes.add(j)
                stack.append(j)
        
    
    
    print("\n --------- Goal found -----------\n")
    for i in way:
        city= identify_city(i)

        if(i!=state):
            print(city," ->",end=" ")
        else:
            print(city,end=" ")

    
# this function allows us to identify the node as a city by his assigned number
def identify_city(i):
    if(i==0):
        city="arad"
    elif(i==1):
        city="zerand"
    elif(i==2):
        city="oradea"
    elif(i==3):
        city="sibiu"
    elif(i==4):
        city="fagaras"
    elif(i==5):
        city="timisora"
    elif(i==6):
        city="lugoj"
    elif(i==7):
        city="mehadia"
    elif(i==8):
        city="dobreta"
    elif(i==9):
        city="craiova"
    elif(i==10):
        city="pisteti"
    elif(i==11):
        city="rimmi"
    elif(i==12):
        city="bucharest"
    
    else:
        city=str(i)
    
    return city



DepthFirstSearch(graph,0,12)

