class Solution(object):
    def letterCombinations(self, digits):
        li = [[],[],['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        res = []
        li1 = []
        if(len(digits) != 0):
            for i in range(len(digits)):
                x = int(digits[i:i+1])
                li1.append(li[x])
            li2 = []
            li2.append(li1[0])
            for i in range(len(li1)-1):
                y = []
                for j in range(len(li2[i])):
                    for k in range(len(li1[i+1])):
                        x = li2[i][j] + li1[i+1][k]
                        y.append(x)
                li2.append(y)
            if(len(digits)> 1):
                return y
            else:
                return li1[0]
            
            
            
                
            
            
        