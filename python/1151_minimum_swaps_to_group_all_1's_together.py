class Solution:
    def minSwaps(self, data: List[int]) -> int:
        one_count = sum(data)
        local_window = 0
        for i in range(one_count):
            local_window += data[i]
        max_window = local_window
        for i in range(1, len(data) - one_count + 1):
            local_window -= data[i-1]
            local_window += data[one_count + i - 1]
            max_window = max(max_window, local_window)
        return one_count - max_window