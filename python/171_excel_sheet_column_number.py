class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        n = len(columnTitle)
        column_number = 0
        norm = ord('A') - 1
        
        for c in columnTitle:
            column_number = column_number * 26 + (ord(c) - norm)
        
        return column_number