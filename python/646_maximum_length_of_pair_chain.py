class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda pair: pair[1])
        total_taken = 1
        last_taken = pairs[0]
        for i in range(len(pairs)):
            if pairs[i][0] > last_taken[1]:
                total_taken += 1
                last_taken = pairs[i]
        return total_taken