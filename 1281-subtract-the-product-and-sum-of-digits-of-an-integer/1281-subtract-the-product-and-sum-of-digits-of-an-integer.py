class Solution(object):
    def subtractProductAndSum(self, n):
        sum = 0
        pro = 1
        while(n > 0):
            sum = sum + n%10
            pro = pro * (n%10)
            n = n / 10
        return (pro-sum)
        