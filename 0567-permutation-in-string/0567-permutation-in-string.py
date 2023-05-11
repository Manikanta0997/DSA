class Solution(object):
    def checkInclusion(self, s1, s2):
        s1d = dict()
        found = 0
        for i in range(len(s1)):
            if s1[i:i+1] in s1d:
                s1d[s1[i:i+1]] += 1
            else:
                s1d[s1[i:i+1]] = 1
        r = len(s1)
        e = dict()
        for i in range(len(s1)):
            if s2[i:i+1] in e:
                e[s2[i:i+1]] += 1
            else:
                e[s2[i:i+1]] = 1
        if e == s1d:
            found = 1
            return True
        else:
            for i in range(len(s2) - len(s1)):
                e[s2[i]] -= 1
                if e[s2[i]] == 0:
                    del e[s2[i]]
                if s2[r] in e:
                    e[s2[r]] += 1
                else:
                    e[s2[r]] = 1
                if e == s1d:
                    found = 1
                    return True
                r += 1
        
                               
                
                
            
        