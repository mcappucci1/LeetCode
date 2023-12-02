class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_length = 0
        chars = sorted(chars)
        for word in words:
            if len(word) > len(chars):
                continue
            word = sorted(word)
            i, j = 0, 0
            while i < len(word) and j < len(chars):
                if word[i] < chars[j]:
                    break
                elif word[i] == chars[j]:
                    i += 1
                j += 1
            if i == len(word):
                total_length += len(word)
        return total_length