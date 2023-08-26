class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        
        for (a, b) in redEdges:
            graph[a].append((b, 0))
        for (a, b) in blueEdges:
            graph[a].append((b, 1))
        
        result = [0] + [-1] * (n - 1)
        q = deque([(0, 0, 0), (0, 1, 0)])
        seen = set([(0, 0), (0,1)])

        while q:
            (node, color, dist) = q.popleft()
            for i, edge in enumerate(graph[node]):
                if edge not in seen and color != edge[1]:
                    if result[edge[0]] == -1:
                        result[edge[0]] = dist + 1
                    seen.add(edge)
                    q.append((edge[0], edge[1], dist + 1))
                
        return result
