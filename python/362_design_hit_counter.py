class HitCounter:

    def __init__(self):
        self.q = []
        self.total = 0

    def hit(self, timestamp: int) -> None:
        if self.q and self.q[-1] == timestamp:
            self.q[-1] = (timestamp, self.q[-1][1] + 1)
        else:
            self.q.append((timestamp, 1))
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        while self.q and self.q[0][0] <= timestamp - 300:
            self.total -= self.q[-1][1]
            self.q.pop(0)
        return self.total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)