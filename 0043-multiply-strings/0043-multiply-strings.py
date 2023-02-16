class Solution(object):
    def multiply(self, num1, num2):
        li = ['0','1','2','3','4','5','6','7','8','9']
        n1 = 0
        n2 = 0
        if(num1 != '0' and num2 != '0'):
            for i in range(len(num1)):
                x = num1[i:i+1]
                for j in range(len(li)):
                    if(x == li[j]):
                        n1 = n1*10 + j
                        break
            for i in range(len(num2)):
                x = num2[i:i+1]
                for j in range(len(li)):
                    if(x == li[j]):
                        n2 = n2*10 + j
                        break
            n1 = n1*n2
            st = ""
            while(n1 > 0):
                st = st + li[n1%10]
                n1 = n1 / 10
            st = st[::-1]
            return st
        else:
            return '0'
            
        
            
        
        