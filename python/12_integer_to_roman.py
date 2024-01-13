class Solution:
    def intToRoman(self, num: int) -> str:

        values = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
            (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        i = 0
        s = ''

        while num > 0:
            while values[i][0] > num:
                i += 1
            s += values[i][1]
            num -= values[i][0]
        
        return s