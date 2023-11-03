class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        n = len(workers)
        m = len(bikes)

        pairs = []
        for w in range(n):
            for b in range(m):
                dist = abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1])
                pairs.append((dist, w, b))

        pairs.sort()

        worker_pair = [-1] * n
        bike_pair = [False] * m
        for dist, worker, bike in pairs:
            if worker_pair[worker] > -1 or bike_pair[bike]:
                continue
            worker_pair[worker] = bike
            bike_pair[bike] = True

        return worker_pair