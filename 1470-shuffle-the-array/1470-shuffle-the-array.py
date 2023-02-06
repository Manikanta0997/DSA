class Solution(object):
    def shuffle(self, nums, n):
        li = []
        for i in range(n):
            li.append(nums[i])
            li.append(nums[n+i])
        return li
        