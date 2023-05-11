class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right = 1
        pro = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                pro = max(pro, prices[right]-prices[left])
            right = right + 1
        return pro
                
            
            
            
        