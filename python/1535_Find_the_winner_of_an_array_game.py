class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        k = min(k, n)
        streak = 0
        curr = 0
        while streak < k:
            nextt = (curr + 1) % n
            if arr[curr] > arr[nextt]:
                streak += 1
                arr[curr], arr[nextt] = arr[nextt], arr[curr]
            else:
                streak = 1
            curr = nextt
        return arr[curr]