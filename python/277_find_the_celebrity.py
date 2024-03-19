# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:

        c = 0

        for i in range(1, n):
            if knows(c, i):
                c = i
        
        for i in range(n):
            if (i != c) and ((knows(c, i)) or (not knows(i, c))):
                return -1
        
        return c
