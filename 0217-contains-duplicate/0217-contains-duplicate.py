class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = dict()
        for i in range(len(nums)):
            if nums[i] in x:
                return True
            else:
                x[nums[i]] = 1
        return False
        