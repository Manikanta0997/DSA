class Solution(object):
    def maxProductDifference(self, nums):
        max1 = 0
        max1i = 0
        max2 = 0
        min1 = 11111
        min1i = 0
        min2 = 11111
        for i in range(len(nums)):
            if(max1 < nums[i]):
                max1 = nums[i]
                max1i = i
            if(min1 > nums[i]):
                min1 = nums[i]
                min1i = i
        print(min1i)
        for i in range(len(nums)):
            if(i != max1i):
                if(max2 < nums[i]):
                    max2 = nums[i]
            if(i != min1i):
                print(i,min1i)
                if(min2 > nums[i]):
                    min2 = nums[i]
        print(max1,max2,min1,min2)
        return (max1 * max2 - min1 * min2)
        