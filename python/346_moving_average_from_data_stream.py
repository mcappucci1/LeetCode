class MovingAverage:

    def __init__(self, size: int):
        self.arr = [0] * size
        self.i = 0
        self.total = 0
        self.full = False
        self.size = size

    def next(self, val: int) -> float:
        self.total += val
        if self.full:
            self.total -= self.arr[self.i]
        self.arr[self.i] = val
        self.full = self.full or self.i == self.size-1
        self.i = (self.i + 1) % self.size
        return self.total / (self.size if self.full else self.i)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)