class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        memo = [True] + [False] * n

        for i in range(n+1):
            if memo[i]:
                for word in wordDict:
                    if len(word) + i > n:
                        continue
                    match = True
                    for j in range(len(word)):
                        if word[j] != s[i + j]:
                            match = False
                            break
                    if match:
                        memo[i+len(word)] = True
        
        return memo[-1]