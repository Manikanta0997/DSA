class Solution(object):
    def numOfPairs(self, nums, target):
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i != j):
                    x = nums[i]
                    x = x + nums[j]
                    if(x == target):
                        count = count + 1
        return count
                
                
                
        