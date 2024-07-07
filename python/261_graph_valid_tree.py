class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False

        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        stack = [(0, None)]
        visited = [True] + [False] * (n-1)
        count = 0

        while stack:
            node, parent = stack.pop()
            count += 1
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                elif visited[neighbor]:
                    return False
                visited[neighbor] = True
                stack.append((neighbor, node))
        
        return count == n