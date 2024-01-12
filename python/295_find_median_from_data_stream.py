class MedianFinder:

    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        if (self.hi and num >= self.hi[0]) or (not self.lo):
            heapq.heappush(self.hi, num)
            if len(self.hi) > len(self.lo):
                e = heapq.heappop(self.hi)
                heapq.heappush(self.lo, -e)
        else:
            heapq.heappush(self.lo, -num)
            if len(self.lo) > len(self.hi)+1:
                e = heapq.heappop(self.lo)
                heapq.heappush(self.hi, -e)

    def findMedian(self) -> float:
        n = len(self.lo) + len(self.hi)
        if n % 2 == 0:
            return (-self.lo[0] + self.hi[0]) / 2
        else:
            return -self.lo[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()