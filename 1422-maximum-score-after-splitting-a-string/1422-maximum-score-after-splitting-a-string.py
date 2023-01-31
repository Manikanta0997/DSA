class Solution(object):
    def maxScore(self, s):
        sum = 0
        li = []
        for i in range(len(s)-1):
            substr = s[0:i+1]
            sub_r = s[i+1:len(s)]
            sum = sum + substr.count('0')
            sum = sum + sub_r.count('1')
            li.append(sum)
            sum = 0
        max = li[0]
        for i in range(len(li)):
            if(li[i] > max):
                max = li[i]
        return max