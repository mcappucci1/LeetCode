class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        n = len(s)
        longest = -1
        indexes = [math.inf] * 26
        norm = ord('a')

        for i in range(n):
            c = ord(s[i]) - norm
            longest = max(longest, i - indexes[c] - 1)
            indexes[c] = min(indexes[c], i)
        
        return longest