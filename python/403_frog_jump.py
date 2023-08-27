class Solution:
    def canCross(self, stones: List[int]) -> bool:

        seen = defaultdict(set)
        seen[0].add(0)
        for stone in stones[:-1]:
            if stone not in seen:
                continue
            for jump_dist in seen[stone]:
                for k in range(-1, 2):
                    if jump_dist + k > 0:
                        seen[stone + jump_dist + k].add(jump_dist + k)
        
        return stones[-1] in seen