class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        m = len(img)
        n = len(img[0])

        copy = [[0] * n for i in range(m)]

        for r in range(m):
            for c in range(n):
                count = 0
                total = 0
                for i in range(max(0, r-1), min(m, r+2)):
                    for j in range(max(0, c-1), min(n, c+2)):
                        total += img[i][j]
                        count += 1
                copy[r][c] = total // count

        return copy