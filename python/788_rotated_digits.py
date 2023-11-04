class Solution:
    def rotatedDigits(self, n: int) -> int:

        num = [0] * 5
        bad = set([3,4,7])
        good = set([2,5,6,9])
        good_count = 0
        bad_count = 0
        total = 0

        def inc(x):
            nonlocal good_count
            nonlocal bad_count
            if x in good: good_count -= 1
            elif x in bad: bad_count -= 1
            if x+1 in good: good_count += 1
            elif x+1 in bad: bad_count += 1

        for x in range(1, n+1):
            inc(num[-1])
            num[-1] += 1
            i = -1
            while num[i] == 10:
                num[i] -= 10
                inc(num[i-1])
                num[i-1] += 1
                i -= 1
            if bad_count == 0 and good_count > 0:
                total += 1

        return total