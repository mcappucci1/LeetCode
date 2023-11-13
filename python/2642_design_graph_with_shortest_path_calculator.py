class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for i in range(n)]
        for u, v, val in edges:
            self.graph[u].append((v,val))


    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1], edge[2]))   


    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2:
            return 0
        vals, heap = [math.inf] * len(self.graph), [(0, node1)]
        while heap:
            score, curr = heapq.heappop(heap)
            if score <= vals[curr]:
                if curr == node2:
                    return score
                for neighbor, val in self.graph[curr]:
                    if score + val < vals[neighbor]:
                        vals[neighbor] = score + val
                        heapq.heappush(heap, (score + val, neighbor))
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)