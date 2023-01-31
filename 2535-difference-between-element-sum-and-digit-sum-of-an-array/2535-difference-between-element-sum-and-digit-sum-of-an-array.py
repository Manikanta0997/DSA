class Solution(object):
    def differenceOfSum(self, nums):
        el = 0
        di = 0
        for i in range(len(nums)):
            el = el + nums[i]
            while(nums[i] > 0):
                di = di + nums[i] % 10
                nums[i] = nums[i] / 10
        return abs(di-el)
        