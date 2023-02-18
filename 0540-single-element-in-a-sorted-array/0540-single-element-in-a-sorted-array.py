class Solution(object):
    def singleNonDuplicate(self, nums):
        x = 0
        found = 0
        if(len(nums) > 1):
            for i in range(len(nums)-1):
                if(nums[x] != nums[x+1]):
                    found = 1
                    return nums[x]
                x = x + 2
                if(x >= len(nums)-1):
                    break
            if(found == 0):
                return nums[len(nums)-1]
        else:
            return nums[x]
                
                
            
        