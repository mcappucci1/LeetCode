class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = [[] for i in range(n)]
        for start, end, cost in flights:
            graph[start].append((end, cost))
        
        q = deque([(src,0)])
        best = [inf] * n

        while q and k >= -1:
            l = len(q)
            for i in range(l):
                node, cost = q.popleft()
                if best[node] < cost:
                    continue
                best[node] = cost
                for end, price in graph[node]:
                    if cost + price < best[end]:
                        best[end] = cost + price
                        q.append((end, cost + price))
            k -= 1
        
        return -1 if best[dst] == inf else best[dst]