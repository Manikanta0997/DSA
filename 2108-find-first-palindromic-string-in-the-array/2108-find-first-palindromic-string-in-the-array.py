class Solution(object):
    def firstPalindrome(self, words):
        found = 0
        for i in range(len(words)):
            x = words[i]
            n = len(x)
            x1 = x[0:len(x)/2]
            if(n%2 != 0):
                x2 = x[len(x)/2 + 1:len(x)]
            else:
                x2 = x[len(x)/2:len(x)]
            x2 = x2[::-1]
            if(x2 == x1):
                found = 1
                break
        if(found == 1):
            return x
        else:
            return ""
            