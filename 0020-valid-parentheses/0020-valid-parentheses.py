class Solution(object):
    def isValid(self, s):
        li = ['(', '[', '{']
        lir = [')', ']','}']
        stack = []
        top = 0
        for i in range(len(s)):
            if s[i] in li:
                if len(stack) <= top:
                    stack.append(s[i])
                else:
                    stack[top] = s[i]
                top = top + 1
            if s[i] in lir:
                if stack == [] or top == 0:
                    top = 100
                    break
                x = stack[top-1]
                x = li.index(x)
                z = lir.index(s[i])
                if x == z:
                    top = top -1
                else:
                    break
        if top == 0:
            return True