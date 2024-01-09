class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        insert = 0
        count = 0
        for c in s:
            if c == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                insert += 1
                count += 1
        return insert + count