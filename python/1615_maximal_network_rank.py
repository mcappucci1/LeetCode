class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for [a, b] in roads:
            graph[a].add(b)
            graph[b].add(a)
        best = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                rank = len(graph[i]) + len(graph[j]) - (0 if i not in graph[j] else 1)
                best = max(best, rank)
        return best