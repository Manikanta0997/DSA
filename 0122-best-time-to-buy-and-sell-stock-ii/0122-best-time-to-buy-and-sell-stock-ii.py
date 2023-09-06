class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot = 0
        i = 0
        r = 1
        pro = 0
        while r < len(prices):
            x = prices[i]
            y = prices[r]
            pro = max(pro, y - x)
            if y <= x or y - x >= pro:
                tot = tot + pro
                i = r
                r+=1
                pro = 0
            else:
                r += 1
        return tot
                    
                    
            
        