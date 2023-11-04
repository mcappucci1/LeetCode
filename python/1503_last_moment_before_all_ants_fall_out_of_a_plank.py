class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        min_right = n if not right else min(right)
        max_left = 0 if not left else max(left)
        return max(n - min_right, max_left)