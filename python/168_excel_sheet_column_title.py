class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ''
        norm = ord('A') - 1
        while columnNumber > 0:
            remainder = (columnNumber - 1) % 26
            columnNumber -= remainder + 1
            columnNumber //= 26
            title = chr(remainder + norm + 1) + title
        return title