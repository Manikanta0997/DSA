class Solution(object):
    def addDigits(self, num):
        def add(num1):
            add = 0
            while(num1 > 0):
                add = add + num1%10
                num1 = num1 / 10
            return add
        while(len(str(num)) > 1):
            num = add(num)
        return num
        
        