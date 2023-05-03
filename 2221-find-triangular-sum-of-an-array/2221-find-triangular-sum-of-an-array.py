class Solution(object):
    def triangularSum(self, nums):
        x = len(nums)
        for i in range(x-1):
            res = []
            for k in range(len(nums)-1):
                z = nums[k]+nums[k+1]
                if(z >= 10):
                    z = z % 10
                res.append(z)
            nums = res
        return nums[0]
        
        