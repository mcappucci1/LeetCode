class UnionFind:
    def __init__(self, grid):
        self.arr = [-1] * (len(grid) * len(grid[0]))

    def union(self, p1, p2):
        p1_parent = self.find(p1)
        p2_parent = self.find(p2)
        if p2_parent == p1_parent:
            return
        if self.arr[p1_parent] < self.arr[p2_parent]:
            self.arr[p1_parent] += self.arr[p2_parent]
            self.arr[p2_parent] = p1_parent
        else:
            self.arr[p2_parent] += self.arr[p1_parent]
            self.arr[p1_parent] = p2_parent

    def find(self, p):
        trav = p
        while self.arr[trav] > -1:
            trav = self.arr[trav]
        while p != trav:
            nextt = self.arr[p]
            self.arr[p] = trav
            p = nextt
        return trav


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        union_find = UnionFind(grid)

        for i in range(m):
            for j in range(n):                
                if grid[i][j] == '1':
                    grid[i][j] = None
                    if i > 0 and grid[i-1][j] == '1':
                        union_find.union((i-1) * n + j, i * n + j)
                    if j > 0 and grid[i][j-1] == '1':
                        union_find.union(i * n + j - 1, i * n + j)
                    if i < m-1 and grid[i+1][j] == '1':
                        union_find.union((i+1) * n + j, i * n + j)
                    if j < n-1 and grid[i][j+1] == '1':
                        union_find.union(i * n + j + 1, i * n + j)
        
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == None and union_find.arr[i * n + j] < 0:
                    num_islands += 1
        
        return num_islands