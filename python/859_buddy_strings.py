class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        dup = False
        seen = 0
        diff = []
        norm = ord('a')
        
        for i in range(len(s)):
            if s[i] != goal[i]:
                if len(diff) == 2:
                    return False
                diff.append(i)
            if not dup:
                mask = 1 << (ord(s[i]) - norm)
                dup = (seen & mask != 0)
                seen |= mask
        
        return (len(diff) == 0 and dup) or (len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]])