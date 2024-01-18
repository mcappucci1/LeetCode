class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        m, n = len(word), len(abbr)
        w = 0
        a = 0
        skip = 0

        while w < m and a < n:
            if abbr[a].isnumeric():
                if skip == 0 and abbr[a] == '0':
                    return False
                skip = skip * 10 + int(abbr[a])
                a += 1
            else:
                if skip > 0:
                    w += skip
                    skip = 0
                    if w >= m:
                        break
                if word[w] != abbr[a]:
                    return False
                w += 1
                a += 1
        
        return (w + skip == m) and (a == n) 