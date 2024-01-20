class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        total = 0
        running = 0
        stack = [-1]

        for i in range(len(arr)):
            while len(stack) > 1 and arr[stack[-1]] >= arr[i]:
                j = stack.pop()
                running -= (j - stack[-1]) * arr[j]
                running += (j - stack[-1]) * arr[i]
            stack.append(i)
            running += arr[i]
            total += running
        
        return total % (pow(10, 9) + 7)