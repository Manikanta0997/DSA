class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        start = 0
        end = n
        index = 0
        for i in range(n):
            mid = (start + end) / 2
            if(mid < n):
                if(target == nums[mid]):
                    index = mid
                    break
                elif(target > nums[mid]):
                    start = mid + 1
                    index = mid + 1
                elif(target < nums[mid]):
                    end = mid - 1
                    index = mid + 1
        if(target > nums[n-1]):
            index = n 
        if(target < nums[0]):
            index = 0
        return index
