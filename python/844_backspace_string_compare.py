class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def handleBackSpace(string, index):
            back_count = 0
            while index > -1 and (string[index] == '#' or back_count > 0):
                back_count += 1 if string[index] == '#' else -1
                index -= 1
            return index

        i, j = len(s) - 1, len(t) - 1
        while i > -1 or j > -1:
            i = handleBackSpace(s, i)
            j = handleBackSpace(t, j)
            if ((i == -1) != (j == -1)) or (i > -1 and s[i] != t[j]):
                return False
            i -= 1
            j -= 1
        
        return True