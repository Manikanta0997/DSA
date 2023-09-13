class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        li = []
        for i in range(len(s)):
            if li and li[-1][0] == s[i:i+1]:
                li[-1][1] += 1
            else:
                li.append([s[i:i+1], 1])
            if li[-1][1] == k:
                li.pop()
        res = ''
        for i, j in li:
            res += i * j
        return res
            
            
            
            
                        
            
        