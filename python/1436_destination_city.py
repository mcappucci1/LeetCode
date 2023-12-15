class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        seen = defaultdict(bool)
        for start, end in paths:
            seen[start] = True
            seen[end] = seen[end]
        
        for city, leaves in seen.items():
            if not leaves:
                return city