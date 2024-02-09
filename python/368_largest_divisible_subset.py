class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        n = len(nums)
        nums.sort()
        length = [1] * n
        index = [-1] * n
        x, m = 0, 1

        for i in range(n):
            for j in range(i-1, -1, -1):
                if (nums[i] % nums[j] == 0) and (length[j] + 1 > length[i]):
                    length[i] = length[j] + 1
                    index[i] = j
                    if length[i] > m:
                        m, x = length[i], i
        
        result = []
        while index[x] != -1:
            result.append(nums[x])
            x = index[x]
        result.append(nums[x])

        return result