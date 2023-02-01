class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count = 0
        li = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i] > nums[j]):
                    count = count + 1
            li.append(count)
            count = 0
        return li