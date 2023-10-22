class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        left = k-1
        right = k+1
        max_score = nums[k]
        min_val = nums[k]

        while (left > -1) or (right < len(nums)):
            if (right == len(nums)) or (left > -1 and nums[left] > nums[right]):
                min_val = min(nums[left], min_val)
                max_score = max(max_score, min_val * (right - left))
                left -= 1
            else:
                min_val = min(nums[right], min_val)
                max_score = max(max_score, min_val * (right - left))
                right += 1
        
        return max_score