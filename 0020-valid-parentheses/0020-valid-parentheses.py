class Solution(object):
    def isValid(self, s):
        op = ['(', '[', '{']
        cl = [')', ']', '}']
        top = 0
        li = []
        for i in range(len(s)):
            if s[i:i+1] in op:
                if top < len(li):
                    li[top] = s[i:i+1]
                    top += 1
                else:
                    li.append(s[i:i+1])
                    top += 1
            else:
                if top > 0:
                    if cl.index(s[i:i+1]) == op.index(li[top-1]):
                        top -= 1
                    else:
                        return False
                else:
                    return False
        if top == 0:
            return True
                    
                
            
        