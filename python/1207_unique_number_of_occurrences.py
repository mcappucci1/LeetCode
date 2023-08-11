class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        seen = set()
        for count in counts.values():
            if count in seen: return False
            seen.add(count)
        return True