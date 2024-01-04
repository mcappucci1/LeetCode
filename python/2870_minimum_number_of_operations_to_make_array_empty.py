class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        total = 0
        for count in counts.values():
            if count == 1:
                return -1
            total += count // 3 + int(count % 3 > 0)
        return total