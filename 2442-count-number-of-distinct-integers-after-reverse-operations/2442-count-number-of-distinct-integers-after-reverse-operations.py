class Solution(object):
    def countDistinctIntegers(self, nums):
        for i in range(len(nums)):
            nums.append(int(str(nums[i])[::-1]))
        return len(set(nums))
        