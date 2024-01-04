class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        counts = [0] * 26
        norm = ord('a')
        for c in s:
            counts[ord(c) - norm] += 1
        
        result = []
        for c in order:
            if counts[ord(c) - norm] > 0:
                result.extend([c] * counts[ord(c) - norm])
                counts[ord(c) - norm] = 0
        for i in range(26):
            if counts[i] > 0:
                result.extend([chr(i+norm)] * counts[i])
        
        return ''.join(result)