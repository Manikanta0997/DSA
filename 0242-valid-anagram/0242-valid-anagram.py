class Solution(object):
    def isAnagram(self, s, t):
        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            x = s[i:i+1]
            if x in dict1:
                dict1[x] += 1
            else:
                dict1[x] = 1
        for i in range(len(t)):
            x = t[i:i+1]
            if x in dict2:
                dict2[x] += 1
            else:
                dict2[x] = 1
        if dict1 == dict2:
            return True
        return False
        

            