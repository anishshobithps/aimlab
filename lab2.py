import heapq

class Graph:
    def __init__(self, graph, heuristic_node_list, start_node):
        self.graph, self.H, self.start = graph, heuristic_node_list, start_node
        self.parent, self.status, self.solution_graph = {}, {}, {}

    def ao_star(self):
        pq = [(0, self.start)]
        while pq:
            cost, v = heapq.heappop(pq)
            if self.status.get(v, 0) == -1:
                continue
            min_cost, child_node_list = self.compute_minimum_cost_child_nodes(v)
            self.H[v] = min_cost
            self.status[v] = len(child_node_list)
            solved = all(self.status.get(child_node, 0) != -1 for child_node in child_node_list)
            if solved:
                self.status[v] = -1
                self.solution_graph[v] = child_node_list
                if v != self.start:
                    heapq.heappush(pq, (self.H[self.parent[v]], self.parent[v]))
            for child_node in child_node_list:
                if self.status.get(child_node, 0) != -1:
                    self.parent[child_node] = v
                    heapq.heappush(pq, (self.H[child_node], child_node))
                    self.status[child_node] = 0

    def compute_minimum_cost_child_nodes(self, v):
        min_cost, min_nodes = float('inf'), []
        for node_info_tuple_list in self.graph.get(v, []):
            cost = sum(self.H.get(c, 0) + weight for c, weight in node_info_tuple_list)
            if cost < min_cost:
                min_cost, min_nodes = cost, [c for c, _ in node_info_tuple_list]
        return min_cost, min_nodes

    def print_solution(self):
        print(f"Starting Node: {self.start}\nSolution: {self.solution_graph}")


h1 = {'A':1,'B':6,'C':2,'D':12,'E':2,'F':1,'G':5,'H':7,'I':7,'J':1,'T':3}
graph1 = {
    'A': [[('B',1),('C',1)],[('D',1)]],
    'B': [[('G',1)],[('H',1)]],
    'C': [[('J',1)]],
    'D': [[('E',1),('F',1)]],
    'G': [[('I',1)]]
}

G1 = Graph(graph1, h1, 'A')
G1.ao_star()
G1.print_solution()