class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        longest = 1
        min_stack = deque([0])
        max_stack = deque([0])
        l, r = 0, 1

        while r < len(nums):
            min_diff = 0 if not min_stack else nums[r] - nums[min_stack[0]]
            max_diff = 0 if not max_stack else nums[max_stack[0]] - nums[r]

            if min_diff <= limit and max_diff <= limit:
                while min_stack and nums[r] < nums[min_stack[-1]]:
                    min_stack.pop()
                min_stack.append(r)
                while max_stack and nums[r] > nums[max_stack[-1]]:
                    max_stack.pop()
                max_stack.append(r)
                r += 1
                longest = max(longest, r - l)
            else:
                l += 1
                if min_stack[0] < l:
                    min_stack.popleft()
                if max_stack[0] < l:
                    max_stack.popleft()
                

        return longest