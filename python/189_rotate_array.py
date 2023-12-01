class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        n = len(nums)
        k %= n

        if k == 0:
            return

        i = 0
        total = 0

        while total < len(nums):
            start = i
            tmp = nums[i]
            while True:
                tmp2 = nums[(i + k) % n]
                nums[(i + k) % n] = tmp
                tmp = tmp2
                i = (i + k) % n
                total += 1
                if i == start:
                    i = i + 1
                    break