
'''

      A     B     C     D    E   F
A     0     2     0     8    0   0
B     2     0     0     5    6   0
C     0     0     0     0    9   3
D     8     5     0     0    3   2
E     0     6     9     3    0   1
F     0     0     3     2    1   0


'''

big_number = 1000


graph = [
   [0,2,0,8,0,0],
   [2,0,0,5,6,0],
   [0,0,0,0,9,3],
   [8,5,0,0,3,2],
   [0,6,9,3,0,1],
   [0,0,3,2,1,0],
]

class Node:

    def __init__(self,name,shortest_distance,previous_node):
        self.name = name
        self.shortest_distance = shortest_distance
        self.previous_node = previous_node
    
    def getName(self):
        return self.name
    
    def getShortestDistance(self):
        return self.shortest_distance
    
    def getPreviousNode(self):
        return self.previous_node
    


def ReportNodes(nodes):

    for i in nodes:
        print("----------------")
        print("Name: ",i.getName())
        print("Shortest Distance: ",i.getShortestDistance())
        print("Preovious Node: ",i.getPreviousNode())


def Dijkstra(graph):

    visited_nodes=set([])
    unvisited_nodes = [0,1,2,3,4,5]
    nodes=[]

    for i in range(len(graph)):
        nodes.append(Node(i,big_number,None))


    #ReportNodes(nodes)

    while len(unvisited_nodes)!=0:
        current_node = unvisited_nodes.pop(0)
        
        if(current_node==0):
            nodes[current_node].shortest_distance = 0

        for index,weight in enumerate(graph[current_node]):

            if(weight !=0 and (index not in visited_nodes)):

                print("neighbor of {} is {} with weigth {}".format(current_node,index,weight))

                if(nodes[index].getShortestDistance() > nodes[current_node].getShortestDistance()+weight):
                    
                    nodes[index].shortest_distance = nodes[current_node].getShortestDistance()+weight
                    nodes[index].previous_node = current_node

        
        visited_nodes.add(current_node)

    ReportNodes(nodes)


Dijkstra(graph)







