class Solution:
    def recTreeDiameter(self, graph, node, parent):
        first, second = -1, -1
        for child in graph[node]:
            if child != parent:
                l = self.recTreeDiameter(graph, child, node)
                if l >= first:
                    second = first
                    first = l
                elif l >= second:
                    second = l
        self.longest = max(self.longest, first + second + 2)
        return first + 1

    def treeDiameter(self, edges: List[List[int]]) -> int:

        n = len(edges) + 1
        graph = [[] for i in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        self.longest = 0

        self.recTreeDiameter(graph, 0, -1)

        return self.longest