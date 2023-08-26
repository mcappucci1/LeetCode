class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:

        result = [0 for i in range(n)]
        graph = defaultdict(list)

        for [a, b] in paths:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        
        for i in range(n):
            if result[i] != 0:
                continue
            if i not in graph:
                result[i] = 1
            colors = [False] * 5
            for neighbor in graph[i]:
                colors[result[neighbor]] = True
            for j in range(4, 0, -1):
                if not colors[j]:
                    result[i] = j
        return result