class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_started = False
        last_word_length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if word_started:
                    return last_word_length
            else:
                word_started = True
                last_word_length += 1
        return last_word_length