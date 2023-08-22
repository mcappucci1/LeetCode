class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        n = len(graph)
        node_states = [0 for i in range(n)]

        def dfs(node, seen):
            nonlocal node_states
            if node_states[node] != 0:
                return node_states[node] == 2
            safe = True
            for neighbor in graph[node]:
                if neighbor in seen:
                    safe = False
                    break
                seen.add(neighbor)
                safe = dfs(neighbor, seen)
                seen.remove(neighbor)
                if not safe:
                    break
            node_states[node] = 2 if safe else 1
            return safe
        
        for i in range(n):
            dfs(i, set([i]))
        
        return [i for i in range(n) if node_states[i] == 2]