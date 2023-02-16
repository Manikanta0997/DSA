class Solution(object):
    def twoSum(self, nums, target):
        hmap = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in hmap:
                break
            else:
                hmap[nums[i]] = i
        li = [hmap[x],i]
        return li
        
        