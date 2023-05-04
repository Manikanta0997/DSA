class Solution(object):
    def isStrictlyPalindromic(self, n):
        flag = "false"
        li = []
        i = -1
        nu = n
        for j in range(2,n-1):
            nu = n
            li2 = []
            count = 0
            while(nu > 0):
                li2.append(nu%j)
                count = count + 1
                i = i + 1
                nu = nu / j
            li.append(li2)
            for k in range(len(li2)/2):
                if(li2[k] != li2[count-1-k]):
                    flag = "false"
        if(flag != "false"):
            return True
            
        