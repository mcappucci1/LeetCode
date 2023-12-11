class Leaderboard:

    def __init__(self):
        self.ids = dict()
        self.scores = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.ids:
            self.ids[playerId] = len(self.scores)
            self.scores.append(score)
        else:
            self.scores[self.ids[playerId]] += score
        

    def top(self, K: int) -> int:
        heap = []
        for score in self.scores:
            if len(heap) < K:
                heapq.heappush(heap, score)
            elif heap[0] < score:
                heapq.heappushpop(heap, score)
        return sum(heap)
        

    def reset(self, playerId: int) -> None:
        self.scores[self.ids[playerId]] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)