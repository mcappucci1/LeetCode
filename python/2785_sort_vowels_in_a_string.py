class Solution:
    def sortVowels(self, s: str) -> str:
        counts = [0] * 10
        vowels = {
            'A':0, 'E':1, 'I':2, 'O':3, 'U':4,
            'a':5, 'e':6, 'i':7, 'o':8, 'u':9
        }
        for c in s:
            if c in vowels:
                counts[vowels[c]] += 1
        
        s = list(s)
        j = 0
        sortedstr = 'AEIOUaeiou'
        for i in range(len(s)):
            if s[i] in vowels:
                while counts[vowels[sortedstr[j]]] == 0:
                    j += 1
                s[i] = sortedstr[j]
                counts[vowels[sortedstr[j]]] -= 1

        return ''.join(s)