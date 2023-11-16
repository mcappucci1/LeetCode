class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set()
        for num in nums:
            seen.add(int(num, 2))
        for i in range(len(nums)+1):
            if i not in seen:
                s = bin(i)[2:]
                return ('0' * (len(nums) - len(s))) + s