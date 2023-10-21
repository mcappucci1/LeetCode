class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        queue = deque([(nums[0], 0)])
        best = nums[0]
        
        for i in range(1, n):
            total = max(queue[0][0] + nums[i], nums[i])
            while queue and total >= queue[-1][0]:
                queue.pop()
            queue.append((total, i))
            if queue[0][1] < i - k + 1:
                queue.popleft()
            best = max(best, queue[0][0])
        
        return best