class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = [nums[0]]
        for i in range(len(nums)):
            if nums[i] > seq[-1]:
                seq.append(nums[i])
            else:
                lo, hi = 0, len(seq)-1
                while lo <= hi:
                    m = (lo + hi) // 2
                    if seq[m] < nums[i]:
                        lo = m+1
                    else:
                        hi = m-1
                seq[lo] = nums[i]
        return len(seq)