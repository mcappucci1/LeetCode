class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_map = [None] * 128
        t_map = [None] * 128

        for i in range(len(s)):
            a, b = ord(s[i]), ord(t[i])
            if (s_map[a] != None and s_map[a] != b) or (t_map[b] != None and t_map[b] != a):
                return False
            s_map[a] = b
            t_map[b] = a
        
        return True