class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts = [0] * 26
        norm = ord('a')
        for i in range(len(s)):
            counts[ord(s[i]) - norm] += 1
            counts[ord(t[i]) - norm] -= 1
        total = 0
        for count in counts:
            total += abs(count)
        return total // 2