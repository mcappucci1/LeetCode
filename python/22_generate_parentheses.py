class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def recGenerate(s, left_count, right_count):
            if left_count == n and right_count == n:
                return [s]
            result = []
            if left_count < n:
                result += recGenerate(s + '(', left_count + 1, right_count)
            if right_count < left_count:
                result += recGenerate(s + ')', left_count, right_count + 1)
            return result
            
        return recGenerate('', 0, 0)