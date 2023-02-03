import math
class Solution(object):
    def numberOfMatches(self, n):
        mat = 0
        while(n>1):
            mat = mat + math.ceil(n/2)
            if(n%2 != 0):
                n = n / 2 + 1
            else:
                n = n / 2
        return int(mat)
        
        