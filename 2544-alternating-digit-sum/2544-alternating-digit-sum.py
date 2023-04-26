class Solution(object):
    def alternateDigitSum(self, n):
        n = str(n)
        n = n[::-1]
        n = int(n)
        res = 0
        i = 0
        while(n>0):
            if(i%2 == 0):
                res = res + n % 10
            else:
                res = res - n%10
            n = n / 10
            i = i + 1
        return res