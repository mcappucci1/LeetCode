class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1,n+1)]
        s = 0
        for i in range(n-1):
            s = (s + k - 1) % len(friends)
            friends.pop(s)
        return friends[0]