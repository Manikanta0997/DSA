class Solution(object):
    def longestConsecutive(self, nums):
        di = {}
        for i in range(len(nums)):
            di[nums[i]] = 1
        ma = 0
        for i in range(len(nums)):
            x = nums[i]
            count = 1
            if ((nums[i] - 1) not in di):
                while x + 1 in di:
                    count += 1
                    x += 1
            if count > ma:
                ma = count
        return ma
                    
                
                
        