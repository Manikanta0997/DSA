class Solution(object):
    def longestConsecutive(self, nums):
        occ = 0
        if(len(nums) > 0):
            x = dict()
            for i in range(len(nums)):
                x[nums[i]] = 1
            for i in range(len(nums)):
                oc = 0
                if nums[i]-1 not in x:
                    while nums[i] in x:
                        oc = oc + 1
                        nums[i] = nums[i] + 1
                if occ < oc:
                    occ = oc
        return occ
                        
                    
            
            
            
        