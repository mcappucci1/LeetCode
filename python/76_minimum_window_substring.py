class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        m = len(s)
        n = len(t)

        if m < n:
            return ''

        t_counts = defaultdict(int)
        for i in range(n):
            t_counts[t[i]] += 1

        mismatch_count = len(t_counts)
        best = None
        s_counts = defaultdict(int)
        l, r = 0, 0

        while r < m:
            while r < m and mismatch_count > 0:
                s_counts[s[r]] += 1
                if s_counts[s[r]] == t_counts[s[r]]:
                    mismatch_count -= 1
                r += 1
            if mismatch_count == 0:
                while l < r and mismatch_count == 0:
                    s_counts[s[l]] -= 1
                    if s_counts[s[l]] < t_counts[s[l]]:
                        mismatch_count += 1
                    l += 1
                if (best == None) or (r - l < best[1] - best[0]):
                    best = (l, r)
        
        return '' if best == None else s[best[0]-1:best[1]]