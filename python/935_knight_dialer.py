class Solution:
    def knightDialer(self, n: int) -> int:

        pad = [1] * 10
        jumps = [[4,6], [6,8], [7,9], [4,8], [0,3,9], [], [0,1,7], [2,6], [1,3], [2,4]]
        for i in range(n-1):
            newPad = [0] * 10
            for i in range(10):
                for j in jumps[i]:
                    newPad[i] += pad[j]
            pad = newPad
        return sum(pad) % (pow(10, 9) + 7)