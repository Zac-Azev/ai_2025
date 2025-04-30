from collections import deque
import heapq

#DISTINÇÃO IMPORTANTE: EU NÃO ESTAVA NA AULA QUANDO VC PASSOU O DOCUMENTO, ENTÃO FIZ DUAS
#BASES DE GRAFOS DIFERENTES, UMA USANDO O ALFABETO E OUTRA USANDO O MAPA DA ROMÊNIA.
#ALGUNS MÉTODOS TIVERAM A IMPLEMENTAÇÃO LEVEMENTE DIFERENTE POR CONTA DE QUE EU SOU 

class Graph:
    def __init__(self):
        self.graphers = {}
    
    def addVertex(self, theGrapher):
        if theGrapher not in self.graphers:
            self.graphers[theGrapher] = []
            
    def addEdge(self, neigh1, neigh2, weight):
        if neigh1 not in self.graphers:
            self.addVertex(neigh1)
        if neigh2 not in self.graphers:
            self.addVertex(neigh2)
        self.graphers[neigh1].append((neigh2, weight))
        
def BFS(graph, begin, end):
    queue = deque([(begin, [begin])])
    already = set()
    
    while queue:
        now, path = queue.popleft()
        if now == end:
            return path
        if now not in already:
            already.add(now)
            for neighbor, _ in graph.graphers[now]:
                queue.append((neighbor, path + [neighbor]))
    return None
        



#ROMENIA-STYLE
def DFS(graph, now, end, path=None, already=None):
    if path is None:
        path = [now]
    if already is None:
        already = set()
        
    if now == end:
        return path
    else:
        already.add(now)
        for neighbor, _ in graph.graphers[now]:
            if neighbor not in already:
                lePath = DFS(graph, neighbor, end, path + [neighbor], already)
                if lePath:
                    return lePath
    return None




#ALPHABET-STYLE
# def DFS(graph, now, end, path=None, already=None):
#     if path is None:
#         path = [now]
#     if already is None:
#         already = set()
        
#     if now == end:
#         return path
#     else:
#         already.add(now)
#         for neighbor, _ in graph.graphers[now]:
#             if neighbor not in already:
#                 lePath = DFS(graph, neighbor, end, path + [neighbor], already)
#             if lePath:
#                 return lePath
#     return None



#ALPHABET-STYLE
#def DJK(graph, begin, end):
#    path = {}
#    requiem = []
#    path[begin] = 0
#
#    heap.heappush(path, [0, begin])
#    
#    while heap:
#        cost, thisNode = heap.heappop(heap)
#
#    if thisNode == objetivo:
#        path = []
#        while thisNode:
#            path.insert(0, thisNode)
#            thisNode = requiem.get(thisNode)
#
#         return path
#
#    for neighbor, weight in graph.graphers[thisNode]:
#        weightedPath = cost + weight
#        if weightPath < path[neighbor]:
#            path[neighbor] = weightPath
#            requiem[neighbor] = thisNode
#            heapq.heappush(heap, (weightPath, neighbor))
#    return None, float('inf')




#ROMENIA-STYLE
def DJK(graph, start, end):
    queue = []
    heapq.heappush(queue, (0, start))  # (distância acumulada, nó atual)
    distances = {start: 0}             # distância mínima conhecida até cada nó
    previous = {}                      # caminho anterior (para reconstrução)

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            # Reconstruir caminho do final para o início
            path = []
            while current_node:
                path.insert(0, current_node)
                current_node = previous.get(current_node)
            return path, distances[end]

        for neighbor, weight in graph.graphers[current_node]:  # ← CORREÇÃO AQUI
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return None, float('inf')  # se não há caminho
    
myGraph = Graph()

#ALPHABET-STYLE
# for letters in range(ord('A'), ord('Z') + 1):
#    myGraph.addVertex(chr(letters))

#ROMENIA-STYLE
romeniaList = ['Arad', 'Zerind', 'Oradea', 'Sibiu', 'Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Rimnicu Vilcea', 'Pitesti', 'Fagaras', 'Bucharest', 'Giurgiu', 'Urziceni', 'Hirsova', 'Eforie', 'Vaslui', 'Iasi', 'Neamt']
for romeniaList in romeniaList:
    myGraph.addVertex(romeniaList)


myEdges = [
#ALPHABET-STYLE
# ('A', 'B', 4), ('A', 'C', 2), ('B', 'D', 5), ('C', 'D', 8), ('C', 'E', 10),
# ('D', 'F', 2), ('E', 'F', 3), ('F', 'G', 1), ('G', 'H', 2), ('H', 'Z', 6),
# ('E', 'I', 2), ('I', 'J', 1), ('J', 'K', 4), ('K', 'L', 3), ('L', 'Z', 5),
# ('L', 'M', 2), ('M', 'N', 3), ('N', 'O', 2), ('O', 'P', 4), ('P', 'Q', 1),
# ('Q', 'R', 5), ('R', 'S', 2), ('S', 'T', 3), ('T', 'U', 2), ('U', 'V', 3),
# ('V', 'W', 1), ('W', 'X', 2), ('X', 'Y', 4), ('Y', 'Z', 3),

#ROMENIA-STYLE
('Arad', 'Zerind', 75),
('Arad', 'Sibiu', 140),
('Arad', 'Timisoara', 118),
('Zerind', 'Arad', 75),
('Zerind', 'Oradea', 71),
('Oradea', 'Zerind', 71),
('Oradea', 'Sibiu', 151),
('Sibiu', 'Arad', 140),
('Sibiu', 'Oradea', 151),
('Sibiu', 'Fagaras', 99),
('Sibiu', 'Rimnicu Vilcea', 80),
('Timisoara', 'Arad', 118),
('Timisoara', 'Lugoj', 111),
('Lugoj', 'Timisoara', 111),
('Lugoj', 'Mehadia', 70),
('Mehadia', 'Lugoj', 70),
('Mehadia', 'Drobeta', 75),
('Drobeta', 'Mehadia', 75),
('Drobeta', 'Craiova', 120),
('Craiova', 'Drobeta', 120),
('Craiova', 'Rimnicu Vilcea', 146),
('Craiova', 'Pitesti', 138),
('Rimnicu Vilcea', 'Sibiu', 80),
('Rimnicu Vilcea', 'Craiova', 146),
('Rimnicu Vilcea', 'Pitesti', 97),
('Pitesti', 'Rimnicu Vilcea', 97),
('Pitesti', 'Craiova', 138),
('Pitesti', 'Bucharest', 101),
('Fagaras', 'Sibiu', 99),
('Fagaras', 'Bucharest', 211),
('Bucharest', 'Fagaras', 211),
('Bucharest', 'Pitesti', 101),
('Bucharest', 'Giurgiu', 90),
('Bucharest', 'Urziceni', 85),
('Giurgiu', 'Bucharest', 90),
('Urziceni', 'Bucharest', 85),
('Urziceni', 'Hirsova', 98),
('Urziceni', 'Vaslui', 142),
('Hirsova', 'Urziceni', 98),
('Hirsova', 'Eforie', 86),
('Eforie', 'Hirsova', 86),
('Vaslui', 'Urziceni', 142),
('Vaslui', 'Iasi', 92),
('Iasi', 'Vaslui', 92),
('Iasi', 'Neamt', 87),
('Neamt', 'Iasi', 87)

]

for neigh1, neigh2, weight in myEdges:
    myGraph.addEdge(neigh1, neigh2, weight)

# print(BFS(myGraph, 'A', 'Z'))
# print(DFS(myGraph, 'A', 'Z'))
# print(DJK(myGraph, 'A', 'Z'))

print(BFS(myGraph, 'Arad', 'Oradea'))
print(DFS(myGraph, 'Arad', 'Oradea'))
print(DJK(myGraph, 'Arad', 'Oradea'))
