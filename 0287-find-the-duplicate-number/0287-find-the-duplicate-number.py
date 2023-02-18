class Solution(object):
    def findDuplicate(self, nums):
        li = []
        for i in range(len(nums)):
            li.append(0)
        for i in range(len(nums)):
            if(li[nums[i]] != 0):
                return nums[i]
            else:
                li[nums[i]] = 1
        