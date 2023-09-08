

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
        state=stack.pop()
        way.append(state)

        for j in range(len(graph[state])):
            #print(graph[state][j],end=" ")
            if(graph[state][j]==1 and j not in visited_nodes):
                
                visited_nodes.add(j)
                stack.append(j)
        
        print(stack)
    
    
    print("\n --------- Goal found -----------\n")
    for i in way:
        city= identify_city(i)

        if(i!=state):
            print(city," ->",end=" ")
        else:
            print(city,end=" ")

    

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

