class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        prefix = 0
        for i in range(len(w)):
            prefix += w[i] / total
            w[i] = prefix
        self.w = w       

    def pickIndex(self) -> int:
        r = random.random()
        lo, hi = 0, len(self.w) - 1
        while lo <= hi:
            m = (hi + lo) // 2
            if r < self.w[m]:
                hi = m - 1
            else:
                lo = m + 1
        return lo


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()