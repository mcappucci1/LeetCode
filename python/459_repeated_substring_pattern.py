class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        n = len(s)
        sub_length = 0
        
        while sub_length < n // 2:
            sub_length += 1
            if n % sub_length != 0:
                continue
            valid = True
            for i in range(sub_length, n, sub_length):
                for j in range(sub_length):
                    if s[j] != s[i+j]:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                return True
        
        return False