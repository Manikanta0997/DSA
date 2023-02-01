class Solution(object):
    def countDigits(self, num):
        count = 0
        n = num
        while(n>0):
            x = n%10
            if(x!=0):
                if(num%x == 0):
                    count = count + 1
            n = n / 10
        return count
        