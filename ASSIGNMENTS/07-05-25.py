#gotta fix that
class Graph:
    def __init__(self):
        self.graphers = {}
    
    def addVertex(self, theGrapher, straightdistance):
        if theGrapher not in self.graphers:
            self.graphers[theGrapher] = []
            self.graphers[theGrapher].append(straightdistance)
            
    def addEdge(self, neigh1, neigh2, weight):
        if neigh1 not in self.graphers:
            self.addVertex(neigh1)
        if neigh2 not in self.graphers:
            self.addVertex(neigh2)
        self.graphers[neigh1].append((neigh2, weight))
        
def Greedy(graph, begin, end, heuristic, where=None, path='Caminho: '):
    lesser = None;
    if where == None:
        where = begin
        path += f"{where}"
    if where == end:
        return path
    else:
        for neighbor, heuristic in graph.graphers.get(where, []):
            if lesser is None:
                lesser = heuristic
                where = neighbor
                path += f" -> {where}"  
            else:
                if weight < lesser:
                    lesser = heuristic
                    where = neighbor
                    path += f" -> {where}"  
        path = Greedy(graph, begin, end, where, path)
    return path
    
#endfunction
myGraph = Graph()

#ROMENIA-STYLE
#romeniaList = ['Arad', 'Zerind', 'Oradea', 'Sibiu', 'Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Rimnicu Vilcea', 'Pitesti', 'Fagaras', 'Bucharest', 'Giurgiu', 'Urziceni', 'Hirsova', 'Eforie', 'Vaslui', 'Iasi', 'Neamt']

distanceToBucharest = [('Arad', 366), ('Zerind', 374), ('Oradea', 380), ('Sibiu', 253), ('Timisoara', 329), ('Lugoj', 244), ('Mehadia', 241), ('Drobeta', 242), ('Craiova', 160), ('Rimnicu Vilcea', 193), ('Pitesti', 1000), ('Fagaras', 178), ('Bucharest', 0), ('Giurgiu', 77), ('Urziceni', 80), ('Hirsova', 151), ('Eforie', 161), ('Vaslui', 199), ('Iasi', 226), ('Neamt', 234)]
for romenia, distance in distanceToBucharest:
    myGraph.addVertex(romenia, distance)


myEdges = [
('Arad', 'Zerind', 75),
('Arad', 'Sibiu', 140),
('Arad', 'Timisoara', 118),
('Zerind', 'Oradea', 71),
('Oradea', 'Sibiu', 151),
('Sibiu', 'Fagaras', 99),
('Sibiu', 'Rimnicu Vilcea', 80),
('Lugoj', 'Timisoara', 111),
('Lugoj', 'Mehadia', 70),
('Mehadia', 'Drobeta', 75),
('Drobeta', 'Craiova', 120),
('Craiova', 'Rimnicu Vilcea', 146),
('Craiova', 'Pitesti', 138),
('Rimnicu Vilcea', 'Pitesti', 97),
('Pitesti', 'Bucharest', 101),
('Fagaras', 'Sibiu', 99),
('Bucharest', 'Fagaras', 211),
('Bucharest', 'Giurgiu', 90),
('Bucharest', 'Urziceni', 85),
('Urziceni', 'Vaslui', 142),
('Hirsova', 'Urziceni', 98),
('Hirsova', 'Eforie', 86),
('Iasi', 'Vaslui', 92),
('Neamt', 'Iasi', 87)
]



for neigh1, neigh2, weight in myEdges:
    myGraph.addEdge(neigh1, neigh2, weight) 
    
print(Greedy(myGraph, 'Arad', 'Oradea', distanceToBucharest))
