# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        r, c = binaryMatrix.dimensions()

        leftmost = c
        for i in range(r):
            if binaryMatrix.get(i, leftmost-1) == 1:
                lo, hi = 0, leftmost-1
                while lo <= hi:
                    m = (hi + lo) // 2
                    if binaryMatrix.get(i, m) == 1:
                        hi = m - 1
                    else:
                        lo = m + 1
                leftmost = lo
                if leftmost == 0:
                    return 0

        return -1 if leftmost == c else leftmost