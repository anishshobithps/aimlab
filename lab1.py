import heapq
from collections import defaultdict

def aStarAlgo(start, goal):
    open_set = [(0, start)]
    g = defaultdict(lambda: float('inf'))
    g[start] = 0
    parents = {}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in parents:
                path.append(current)
                current = parents[current]
            path.append(start)
            print('Path found:', path[::-1])
            return path
        
        for neighbor, weight in graph.get(current, []):
            tentative_g = g[current] + weight
            if tentative_g < g[neighbor]:
                parents[neighbor] = current
                g[neighbor] = tentative_g
                heapq.heappush(open_set, (tentative_g + heuristic(neighbor, goal), neighbor))
    
    print('Path doesn\'t exist!')
    return None

def heuristic(node, goal):
    return {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0
    }.get(node, float('inf'))

graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('G', 9)],
    'E': [('D', 6)],
    'D': [('G', 1)]
}

aStarAlgo('A', 'G')