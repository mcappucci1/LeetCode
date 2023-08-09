class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        char_indexes = dict()
        substring_start = 0
        for i in range(len(s)):
            if s[i] in char_indexes and char_indexes[s[i]] >= substring_start:
                substring_start = char_indexes[s[i]] + 1
            char_indexes[s[i]] = i
            longest_substring = max(longest_substring, i - substring_start + 1)
        return longest_substring