class Solution(object):
    def rearrangeArray(self, nums):
        pos = []
        neg = []
        for i in range(len(nums)):
            if(nums[i] > 0):
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        j=0
        for i in range(len(nums)/2):
            nums[j] = pos[i]
            j = j + 1
            nums[j] = neg[i]
            j = j + 1
            
        return nums