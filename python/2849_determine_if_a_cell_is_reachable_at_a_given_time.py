class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:
            return False
        total_dist = max(abs(sx - fx), abs(sy - fy))
        return total_dist <= t