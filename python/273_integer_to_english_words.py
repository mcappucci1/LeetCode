class Solution:
    def numberToWords(self, num: int) -> str:
        
        if num == 0:
            return 'Zero'

        s = ''
        place = 0
        ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        teens = {
            10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'
        }
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        places = ['Hundred', 'Thousand', 'Million', 'Billion']

        while num:
            x = num % 1000
            # place
            if (place > 0) and (x > 0):
                 s = places[place] + ' ' + s
            # teens
            if (10 <= x % 100 <= 19):
                s = teens[x % 100] + ' ' + s
            else:
                if 0 < x % 10:
                    s = ones[x % 10] + ' ' + s
                if 20 <= x % 100:
                    s = tens[x % 100 // 10] + ' ' + s
            if x // 100 > 0:
                s = ones[x // 100] + ' Hundred ' + s
            num //= 1000
            place += 1

        return s[:-1]