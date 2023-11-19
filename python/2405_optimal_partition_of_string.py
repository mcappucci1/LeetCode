class Solution:
    def partitionString(self, s: str) -> int:
        splits = 1
        seen = 0
        norm = ord('a')
        for c in s:
            mask = 1 << (ord(c) - norm)
            if seen & mask:
                seen = mask
                splits += 1
            else:
                seen |= mask
        return splits