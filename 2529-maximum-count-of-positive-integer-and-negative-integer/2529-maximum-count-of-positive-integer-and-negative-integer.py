class Solution(object):
    def maximumCount(self, nums):
        lenneg = 0
        lenpos = 0
        for i in nums:
            if(i > 0):
                lenpos = lenpos + 1
            elif(i<0):
                lenneg = lenneg + 1
        if(lenneg > lenpos):
            lenpos = lenneg
        return lenpos            
        