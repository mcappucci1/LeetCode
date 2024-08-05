class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = defaultdict(int)
        for s in arr:
            counts[s] += 1
        for s in counts.keys():
            if counts[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ''