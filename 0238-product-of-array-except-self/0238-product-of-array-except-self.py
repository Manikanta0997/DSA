class Solution(object):
    def productExceptSelf(self, nums):
        prefix = []
        postfix = []
        mul1 = 1
        mul2 = 1
        res = []
        if(len(nums)>2):
            for i in range(len(nums)):
                mul1 = mul1*nums[i]
                mul2 = mul2*nums[len(nums)-1-i]
                prefix.append(mul1)
                postfix.append(mul2)
            for i in range(len(postfix)/2):
                temp = postfix[i]
                postfix[i] = postfix[len(postfix)-1-i]
                postfix[len(postfix)-1-i] = temp
            res.append(postfix[1])
            for i in range(1,len(nums)-1):
                mul = prefix[i-1] * postfix[i+1]
                res.append(mul)
            res.append(prefix[len(nums)-2])
            return res
        else:
            temp = nums[0]
            nums[0] = nums[1]
            nums[1] = temp
            return nums
            
        