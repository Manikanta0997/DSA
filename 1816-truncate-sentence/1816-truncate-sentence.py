class Solution(object):
    def truncateSentence(self, s, k):
        li = s.split()
        s = ""
        for i in range(k):
            s = s + " " +li[i]
        s = s[1:]
        return s
        