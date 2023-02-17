class Solution(object):
    def countGoodSubstrings(self, s):
        count = 0
        for i in range(len(s)-2):
            li = []
            li.append(s[i:i+1])
            li.append(s[i+1:i+2])
            li.append(s[i+2:i+3])
            x = set(li)
            if(len(x) == 3):
                count = count + 1
        return count 
            