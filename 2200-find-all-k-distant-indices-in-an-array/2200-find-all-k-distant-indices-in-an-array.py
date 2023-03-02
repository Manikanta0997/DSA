class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        index = []
        for i in range(len(nums)):
            if(nums[i] == key):
                index.append(i)
        li = []
        for j in range(len(nums)):
            for z in range(len(index)):
                if(abs(j-index[z])<=k):
                    li.append(j)
        li = set(li)
        li = list(li)
        li.sort()
        return li
        