class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right = 1
        pro = 0
        while right < len(prices):
            x = prices[left]
            y = prices[right]
            if x >= y:
                left += 1
                right += 1
            elif y > x:
                while y > x:
                    pro = max(pro, y-x)
                    right = right + 1
                    if right == len(prices):
                        break
                    y = prices[right]
                left = right
                right += 1
        return pro
                
            
            
            
        