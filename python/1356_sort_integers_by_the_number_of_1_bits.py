class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def sortCB(x):
            total = 1
            while x:
                total += 1
                x &= x - 1
            return total
        
        arr.sort(key=lambda x: (sortCB(x), x))
        return arr