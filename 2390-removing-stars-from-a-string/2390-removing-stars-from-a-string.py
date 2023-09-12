class Solution:
    def removeStars(self, s: str) -> str:
        res = ""
        li =[]
        top = 0
        for i in range(len(s)):
            if s[i:i+1] != '*':
                if top < len(li):
                    li[top] = s[i:i+1]
                else:
                    li.append(s[i:i+1])
                top += 1
            else:
                top -= 1
        for i in range(top):
            res += li[i]
        return res
                    