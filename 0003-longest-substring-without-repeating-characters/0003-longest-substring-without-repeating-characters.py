class Solution(object):
    def lengthOfLongestSubstring(self, s):
        x = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in x:
                x.remove(s[l])
                l = l + 1
            x.add(s[r])
            res = max(res, r-l+1)
        return res
                
            
                