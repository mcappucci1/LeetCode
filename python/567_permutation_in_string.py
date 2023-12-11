class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        m, n = len(s2), len(s1)
        
        # Can't have perm if s1 is too small
        if m < n:
            return False
        
        # Get counts of s2 (permutation)
        s1_counts = [0] * 26
        norm = ord('a')
        for c in s1:
            s1_counts[ord(c) - norm] += 1
        
        # Get counts of first substring of s1
        s2_counts = [0] * 26
        for i in range(n):
            s2_counts[ord(s2[i]) - norm] += 1
        
        # How many chars are off
        num_mismatch = 0
        for i in range(26):
            if s2_counts[i] < s1_counts[i]:
                num_mismatch += 1
        
        i = n
        while num_mismatch > 0 and i < m:
            add = ord(s2[i]) - norm
            sub = ord(s2[i - n]) - norm
            s2_counts[add] += 1
            if s2_counts[add] == s1_counts[add]:
                num_mismatch -= 1
            if s2_counts[sub] == s1_counts[sub]:
                num_mismatch += 1
            s2_counts[sub] -= 1
            i += 1
        
        return num_mismatch == 0