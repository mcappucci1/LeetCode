class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:

        n = len(arr)
        arr.sort()
        memo = [1] * n
        total = 0
        indexes = dict()

        for i in range(n):
            indexes[arr[i]] = i

        for i in range(n):
            bound = math.sqrt(arr[i])
            j = 0
            while j < i and arr[j] <= bound:
                if (arr[i] % arr[j] == 0) and ((arr[i] // arr[j]) in indexes):
                    k = indexes[arr[i] // arr[j]]
                    memo[i] += (1 if j == k else 2) * memo[j] * memo[k]
                j += 1
            total += memo[i]

        return total % (10 ** 9 + 7)