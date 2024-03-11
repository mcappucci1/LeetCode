class Solution:
    def customSortString(self, order: str, s: str) -> str:
        return ''.join(sorted(s, key=lambda c: order.index(c) if c in order else inf))