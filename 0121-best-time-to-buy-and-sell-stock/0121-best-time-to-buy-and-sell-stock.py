class Solution(object):
    def maxProfit(self, prices):
        l = 0
        r = 1
        max1 = 0
        while(r < len(prices) and l < len(prices)):
            x = prices[r] - prices[l] 
            if x > max1:
                max1 = x
            elif prices[l] > prices[r]:
                l = r
                r = r + 1
            else:
                r = r + 1
        return max1
        