class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        return sorted(nums, key=lambda num: (counts[num], -num))