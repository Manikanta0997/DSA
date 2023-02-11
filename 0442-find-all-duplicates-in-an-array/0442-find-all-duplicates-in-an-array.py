class Solution(object):
    def findDuplicates(self, nums):
        n = len(nums)
        li = []
        for i in range(n):
            li.append(i+1)
        res = []
        print(li)
        for i in range(n):
            x = nums[i]
            if(li[x-1] != 0):
                li[x-1] = 0
            else:
                res.append(x)
        return res
        