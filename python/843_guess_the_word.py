class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        
        while True:
            x = random.randint(0, len(words)-1)
            words[-1], words[x] = words[x], words[-1]
            match = master.guess(words[-1])
            if match == len(words[-1]):
                return words[-1]
            compare = words.pop()
            i = 0
            while i < len(words):
                matching = 0
                for j in range(len(compare)):
                    if compare[j] == words[i][j]:
                        matching += 1
                if matching != match:
                    words[-1], words[i] = words[i], words[-1]
                    words.pop()
                else:
                    i += 1