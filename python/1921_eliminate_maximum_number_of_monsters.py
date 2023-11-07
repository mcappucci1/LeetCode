class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        n = len(speed)
        buckets = [0 for i in range (n+1)]
        for i in range(n):
            time = math.ceil(dist[i] / speed[i])
            if time <= n:
                buckets[time] += 1
        
        next_shot = 0
        for i in range(n):
            if buckets[i] > 0:
                if next_shot + (buckets[i] - 1) >= i:
                    return i
                next_shot += buckets[i]

        return n