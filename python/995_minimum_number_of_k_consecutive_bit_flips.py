class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:

        n = len(nums)
        total = 0
        carry = 0
        swaps = deque()

        for i in range(n-k+1):
            if swaps and swaps[0] <= i-k:
                swaps.popleft()
                carry ^= 1
            if nums[i] ^ carry == 0:
                carry ^= 1
                swaps.append(i)
                total += 1

        for i in range(n-k+1, n):
            if swaps and swaps[0] <= i-k:
                swaps.popleft()
                carry ^= 1
            if nums[i] ^ carry == 0:
                return -1
        
        return total