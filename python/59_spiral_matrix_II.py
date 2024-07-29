class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:        
        
        matrix = [[0] * n for i in range(n)]
        tr, br, lc, rc = 0, n-1, 0, n-1
        cell = 1
        
        for loop in range((n+1) // 2):
            for i in range(lc, rc+1):
                matrix[tr][i] = cell
                cell += 1
            tr += 1
            for i in range(tr, br+1):
                matrix[i][rc] = cell
                cell += 1
            rc -= 1
            for i in range(rc, lc-1, -1):
                matrix[br][i] = cell
                cell += 1
            br -= 1
            for i in range(br, tr-1, -1):
                matrix[i][lc] = cell
                cell += 1
            lc += 1
                
        return matrix