class Solution:
    def isNumber(self, s: str) -> bool:

        seenNum, seenExp, seenDec = False, False, False

        for i, c in enumerate(s):
            if c.isnumeric():
                seenNum = True
            elif c.lower() == 'e':
                if (not seenNum) or seenExp:
                    return False
                seenExp = True
                seenNum = False
            elif c == '-' or c =='+':
                if i > 0 and s[i-1].lower() != 'e':
                    return False
            elif c == '.':
                if seenDec or seenExp:
                    return False
                seenDec = True
            else:
                return False

        return seenNum