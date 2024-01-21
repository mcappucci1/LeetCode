class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s)

        def reverseWord(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        l = 0
        for i in range(n):
            if s[i] == ' ':
                if l < i - 1:
                    reverseWord(l, i-1)
                l = i + 1

        if l == 0:
            return

        if l < n - 1:
            reverseWord(l, n - 1)


        for i in range(n // 2):
            s[i], s[n-i-1] = s[n-i-1], s[i]