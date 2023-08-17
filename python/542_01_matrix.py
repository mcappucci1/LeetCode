class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m = len(mat)
        n = len(mat[0])
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    mat[i][j] = min(
                        (float('inf') if i == 0 else mat[i-1][j] + 1),
                        (float('inf') if j == 0 else mat[i][j-1] + 1)
                    )
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if mat[i][j] != 0:
                    mat[i][j] = min(
                        mat[i][j],
                        (float('inf') if i == m-1 else mat[i+1][j] + 1),
                        (float('inf') if j == n-1 else mat[i][j+1] + 1)
                    )
        return mat