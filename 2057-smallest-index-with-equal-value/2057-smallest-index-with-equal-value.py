class Solution(object):
    def smallestEqual(self, nums):
        found = 0
        for i in range(len(nums)):
            if(nums[0]==0):
                found = 1
                index = i
                break
            if(i%10 == nums[i]):
                found = 1
                index = i
                break
        if(found == 0):
            return -1
        else:
            return index
        