class Solution(object):
    def numberOfSteps(self, num):
        step = 0
        while(num > 0):
            if(num %2 == 0):
                step = step + 1
                num = num / 2
            else:
                num = num - 1
                step = step + 1
        return step
                