class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_string = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        def generateStrings(s, i, strs):
            nonlocal digit_to_string
            nonlocal digits
            if i == len(digits):
                if s != '':
                    strs.append(s)
                return
            for letter in digit_to_string[digits[i]]:
                generateStrings(s + letter, i + 1, strs)
        
        strs = []
        generateStrings('', 0, strs)
        return strs
