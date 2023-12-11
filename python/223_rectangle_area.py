class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x_intersect = max((min(ax2,bx2) - bx1) if ax1 <= bx1 <= ax2 else 0, (min(bx2,ax2) - ax1) if bx1 <= ax1 <= bx2 else 0)
        y_intersect = max((min(ay2,by2) - by1) if ay1 <= by1 <= ay2 else 0, (min(by2,ay2) - ay1) if by1 <= ay1 <= by2 else 0)
        return ((ax2 - ax1) * (ay2 - ay1)) + ((bx2 - bx1) * (by2 - by1)) - (x_intersect * y_intersect)