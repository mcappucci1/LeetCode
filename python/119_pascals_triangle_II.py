class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            for j in range(1, len(row)):
                row[j] = row[j-1] + row[j]
            row.append(1)
        return row