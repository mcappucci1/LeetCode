class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        n = len(fruits)
        max_fruit = 0
        seen_types = dict()
        
        l = 0
        for r in range(n):
            if fruits[r] not in seen_types:
                if len(seen_types) == 2:
                    max_fruit = max(max_fruit, r - l)
                    remove = min(seen_types, key=seen_types.get)
                    l = seen_types[remove] + 1
                    del seen_types[remove]
            seen_types[fruits[r]] = r
        
        max_fruit = max(max_fruit, r - l + 1)
        
        return max_fruit