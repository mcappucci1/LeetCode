class Solution:
    def countVowelPermutation(self, n: int) -> int:
        counts = [1] * 5
        for x in range(1, n):
            [a, e, i, o, u] = counts
            counts[0] = e + i + u
            counts[1] = a + i
            counts[2] = e + o
            counts[3] = i
            counts[4] = i + o
        return sum(counts) % (10 ** 9 + 7)