import sys # Used to assign the infinite cost to all the nodes apart from the source node
from heapq import heapify, heappush, heappop

def dijkstra(graph, src, dest):
    infinite = sys.maxsize
    node_data = {
        'A' : {'cost': infinite, 'pred':[] },
        'B' : {'cost': infinite, 'pred':[] },
        'C' : {'cost': infinite, 'pred':[] },
        'D' : {'cost': infinite, 'pred':[] },
        'E' : {'cost': infinite, 'pred':[] },
        'F' : {'cost': infinite, 'pred':[] }
    }
    node_data[src]['cost'] = 0
    #Create a list of visited nodes
    visited = []
    temp = src # To reassign the source to the node that has the minimum cost
    for i in range(5):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in graph[temp]: # To traverse the neighbours
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost 
                        # This reassigns the cost of the node in thr node_data to the new cost if that new cost is lower than the previous cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)
                        # This is to add the source as the predecessors of its adjascent nodes 
                    heappush(min_heap, (node_data[j]['cost'], j))
        heapify(min_heap)
        temp = min_heap[0][1]
    print(f"Shortest Distance: {node_data[dest]['cost']}")
    print(f"Shortest Path: {node_data[dest]['pred'] + list(dest)}")

# Draw the graph in the question
graph = {
    'A':{'B':3, 'D':8},
    'B':{'A':3, 'D':5, 'E':6},
    'C':{'E':9, 'F':3},
    'D':{'A':8, 'B':5, 'E':3, 'F':2},
    'E':{'B':6, 'D':3, 'F':1, 'C':9},
    'F':{'D':2, 'E':1, 'C':3},
} 

source = "A"
destination = "C"
dijkstra(graph, source, destination)



