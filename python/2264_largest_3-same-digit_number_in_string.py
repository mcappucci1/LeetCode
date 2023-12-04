class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = ''
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i+1] == num[i+2] and num[i] > largest:
                largest = num[i]
        return largest and (largest * 3)