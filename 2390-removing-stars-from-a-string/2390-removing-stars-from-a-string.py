class Solution(object):
    def removeStars(self, s):
        li = []
        for i in range(len(s)):
            li.append(s[i:i+1])
        x = ''
        for i in range(len(li)):
            if(li[i] != '*'):
                x = x + li[i]
            if(li[i] == '*'):
                x = x[0:len(x)-1]
        return x
        