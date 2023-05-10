class Solution(object):
    def sumOfThree(self, num):
        li = []
        if num%3==0:
            x = num / 3
            li = [x-1,x,x+1]
        return li
        
        