from collections import deque

class Graph:
    def __init__(self):
        self.graphers = {}
    
    def addVertex(self, theGrapher):
        if theGrapher not in self.graphers:
            self.graphers[theGrapher] = []
            
    def addEdge(self, neigh1, neigh2, weight):
        if neigh1 not in self.graphers:
            self.addVertex(neigh1)
        else if neigh2 not in self.graphers:
            self.addVertex(neigh2)
        self.graphers[neigh1].append((neigh2, weight))
        
    def BFS(graph, begin, end):
        queue = deque([(begin, [begin])])
        already = set()
        
        while queue:
            now, path = queue.popleft()
            if now == end:
                return path
            else if now not in already:
                already.add(now)
                for neighbor, _ in graph.graphers[now]:
                    queue.append((neighbor, path + [neighbor]))
        return None
        
        
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
                    
    def DJK(graph, begin, end):
        path = {node: float 'inf' for node in graph.graphers}
        requiem = {]
        path[begin] = 0
        
        heap = [(0, begin)]
        
        while heap:
        cost, thisNode = heapq.heappop(heap)

        if thisNode == objetivo:
            path = []
            while thisNode:
                path.insert(0, thisNode)
                thisNode = requiem.get(thisNode)
            return path

        for neighbor, weight in graph.graphers[thisNode]:
            weightedPath = cost + weight
            if weightPath < path[neighbor]:
                path[neighbor] = weightPath
                requiem[neighbor] = thisNode
                heapq.heappush(heap, (weightPath, neighbor))
    return None, float('inf')
        
    myGraph = Graph()
    for letters in range(ord('A'), ord('Z') + 1):
    myGraph.addVertex(chr(letters))
    
    myEdges = [
    ('A', 'B', 4), ('A', 'C', 2), ('B', 'D', 5), ('C', 'D', 8), ('C', 'E', 10),
    ('D', 'F', 2), ('E', 'F', 3), ('F', 'G', 1), ('G', 'H', 2), ('H', 'Z', 6),
    ('E', 'I', 2), ('I', 'J', 1), ('J', 'K', 4), ('K', 'L', 3), ('L', 'Z', 5),
    ('L', 'M', 2), ('M', 'N', 3), ('N', 'O', 2), ('O', 'P', 4), ('P', 'Q', 1),
    ('Q', 'R', 5), ('R', 'S', 2), ('S', 'T', 3), ('T', 'U', 2), ('U', 'V', 3),
    ('V', 'W', 1), ('W', 'X', 2), ('X', 'Y', 4), ('Y', 'Z', 3),
]

for neigh1, neigh2, weight in arestas:
    myGraph.addEdge(neigh1, neigh2, weight)
    
    print(BFS(graph, 'A', 'Z'))
    print(DFS(graph, 'A', 'Z'))
    print(DJK(graph, 'A', 'Z'))
    
