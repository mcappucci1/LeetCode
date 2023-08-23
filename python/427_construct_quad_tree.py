"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def recBuildQuadTree(x, y, length):

            if length == 1:
                return (Node(grid[y][x] == 1, True), grid[y][x])

            half = length // 2
            top_left = recBuildQuadTree(x, y, half)
            top_right = recBuildQuadTree(x + half, y, half)
            bottom_left = recBuildQuadTree(x, y + half, half)
            bottom_right = recBuildQuadTree(x + half, y + half, half)
            
            if top_left[1] != None and top_left[1] == top_right[1] == bottom_right[1] == bottom_left[1]:
                return (Node(top_left[1] == 1, True), top_left[1])
            
            return (Node(True, False, top_left[0], top_right[0], bottom_left[0], bottom_right[0]), None)
        
        return recBuildQuadTree(0, 0, len(grid))[0]

        