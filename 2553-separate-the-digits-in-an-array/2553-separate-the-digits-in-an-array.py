class Solution(object):
    def separateDigits(self, nums):
        res = []
        for i in range(len(nums)):
            x = nums[i]
            li = []
            while(x > 0):
                li.append(x % 10)
                x = x / 10
            for j in range(len(li)):
                res.append(li[len(li)-j-1])
        return res
            
        