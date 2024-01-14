class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        m = len(num1)
        n = len(num2)
        
        result = [0] * (m + n)
        mult1 = m
        
        for i in range(m-1, -1, -1):
            a = int(num1[i])
            mult2 = n-1
            for j in range(n-1, -1, -1):
                b = int(num2[j])
                result[mult1 + mult2] += a * b
                mult2 -= 1
            mult1 -= 1
            
        for i in range(m + n - 1, 0, -1):
            result[i-1] += result[i] // 10
            result[i] = str(result[i] % 10)
        
        result[0] = str(result[0])
        
        for i in range(m+n-1):
            if result[i] != '0':
                break
            result[i] = ''
        
        return ''.join(result)