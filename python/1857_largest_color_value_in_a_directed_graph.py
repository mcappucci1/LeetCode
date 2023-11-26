class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        n = len(colors)
        indegree = [0] * n
        graph = [[] for i in range(n)]

        for s, e in edges:
            graph[s].append(e)
            indegree[e] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        counts = [[0] * 26 for i in range(n)]
        seen = 0
        best = 0
        norm = ord('a')

        while q:
            node = q.popleft()
            seen += 1
            counts[node][ord(colors[node]) - norm] += 1
            best = max(best, counts[node][ord(colors[node]) - norm])
            for neighbor in graph[node]:
                for i in range(26):
                    counts[neighbor][i] = max(counts[node][i], counts[neighbor][i])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return best if seen == n else -1