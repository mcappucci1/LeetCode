class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = [0 for i in range(26)]
        norm = ord('a')
        for i in range(len(s)):
            counts[ord(s[i]) - norm] += 1
            counts[ord(t[i]) - norm] -= 1
        for x in counts:
            if x != 0:
                return False
        return True
