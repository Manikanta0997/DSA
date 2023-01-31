class Solution(object):
    def shuffle(self, nums, n):
        li =[]
        for i in range(len(nums)/2):
            li.append(nums[i])
            li.append(nums[len(nums)/2 + i])
        return li
        