class Solution(object):
    def signFunc(self, x):
        if(x > 0):
            return 1
        elif(x <0):
            return -1
        else:
            return 0
    def arraySign(self, nums):
        mul = 1
        for i in range(len(nums)):
            mul = mul * nums[i]
        return self.signFunc(mul)