class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # Queue of max elements
        queue = deque([])

        # Fill the initial queue
        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        
        # Solution array
        answer = [nums[queue[0]]]
        for i in range(k, len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            while queue and queue[0] < (i - k + 1):
                queue.popleft()
            answer.append(nums[queue[0]])

        return answer