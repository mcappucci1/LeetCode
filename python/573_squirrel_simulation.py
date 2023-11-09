class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        
        total = 0
        best_diff = -float('inf')

        for nut in nuts:
            nut_to_tree = abs(nut[0] - tree[0]) + abs(nut[1] - tree[1])
            squirrel_to_nut = abs(nut[0] - squirrel[0]) + abs(nut[1] - squirrel[1])
            total += nut_to_tree * 2
            best_diff = max(best_diff, nut_to_tree - squirrel_to_nut)

        return total - best_diff