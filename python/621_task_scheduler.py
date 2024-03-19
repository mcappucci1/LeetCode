class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = [0] * 26
        norm = ord('A')

        for task in tasks:
            counts[ord(task) - norm] += 1
        
        counts = [-count for count in counts if count > 0]
        heapq.heapify(counts)
        q = deque()

        total = 0
        while counts or q:
            total += 1
            if q and q[0][1] <= total:
                val, _ = q.popleft()
                heapq.heappush(counts, val)
            if counts:
                most = heapq.heappop(counts)
                if most < -1:
                    most += 1
                    q.append((most, total + n + 1))
            else:
                total = q[0][1] - 1
        
        return total