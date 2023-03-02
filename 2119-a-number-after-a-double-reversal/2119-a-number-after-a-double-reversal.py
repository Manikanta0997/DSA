class Solution(object):
    def isSameAfterReversals(self, num):
        if(num%10 != 0 or num == 0):
            return 'true'
        