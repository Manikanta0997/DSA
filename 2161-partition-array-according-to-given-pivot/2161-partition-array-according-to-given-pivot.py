class Solution(object):
    def pivotArray(self, nums, pivot):
        gre = []
        les = []
        eq = []
        for i in range(len(nums)):
            if(nums [i] > pivot):
                gre.append(nums[i])
            elif(nums[i] == pivot):
                eq.append(nums[i])
            else:
                les.append(nums[i])
        for i in range(len(eq)):
            les.append(eq[i])
        for i in range(len(gre)):
            les.append(gre[i])
        return les