class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def recGenerate(k):
            if k == 1:
                return ['()']
            result = set()
            for i in range(1, k):
                left = recGenerate(i)
                right = recGenerate(k-i)
                for l in left:
                    for r in right:
                        result.add(l + r)
                    if i == k-1:
                        result.add('(' + l + ')')
            return result

            
        return recGenerate(n)