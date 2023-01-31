class Solution(object):
    def smallestEvenMultiple(self, n):
        mul = 0
        if(n%2 == 0):
            mul = n
        else:
            i=2
            while(mul == 0):
                n = n * i
                i = i + 1
                if(n%2 == 0):
                    mul = n
        return n
                
        