class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(list('aeiouAEIOU'))
        a_vowel_count = 0
        b_vowel_count = 0
        half = len(s) // 2

        for i in range(half):
            if s[i] in vowels:
                a_vowel_count += 1
            if s[i + half] in vowels:
                b_vowel_count += 1
        
        return a_vowel_count == b_vowel_count