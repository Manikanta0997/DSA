class Solution(object):
    def getLucky(self, s, k):
        li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        num = ''
        for i in range(len(s)):
            x = s[i:i+1]
            num = num + str(li.index(x)+1) 
        num = int(num)
        res = 0
        for i in range(k):
            while(num > 0):
                res = res + num%10
                num = num / 10
            num = res
            res = 0
        return num
            
            