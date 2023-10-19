class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        graph = defaultdict(lambda: [[],[]])

        for (start, end) in connections:
            graph[start][0].append(end)
            graph[end][1].append(start)
        
        num_changed = 0
        seen = set([0])
        stack = [0]

        while stack:
            curr = graph[stack.pop()]
            for outbound in curr[0]:
                if outbound not in seen:
                    seen.add(outbound)
                    num_changed += 1
                    stack.append(outbound)
            for inbound in curr[1]:
                if inbound not in seen:
                    seen.add(inbound)
                    stack.append(inbound)

        return num_changed