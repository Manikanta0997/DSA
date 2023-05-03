class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        add = 0
        count = 0
        for i in range(len(costs)):
            if(add > coins):
                break
            else:
                add = add + costs[i]
                if(add <= coins):
                    count = count + 1
        return count
        