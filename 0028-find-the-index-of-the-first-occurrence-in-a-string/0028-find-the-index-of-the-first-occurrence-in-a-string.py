class Solution(object):
    def strStr(self, haystack, needle):
        x = len(needle)
        y = len(haystack)
        found = 0
        if(y > x):
            for i in range(y-x+1):
                w = haystack[i:i+x]
                print(w)
                if(w == needle):
                    found = 1
                    break
        if(y == x):
            if(haystack == needle):
                found = 1
                i = 0
        if(found == 0):
            return -1
        elif(found == 1):
            return i
        