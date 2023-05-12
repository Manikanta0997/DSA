class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        res = []
        def backtrack(opene, close):
            if opene == close == n:
                res.append("".join(stack))
                return
            if opene < n:
                stack.append('(')
                backtrack(opene+1, close)
                stack.pop()
            if close < opene:
                stack.append(')')
                backtrack(opene, close+1)
                stack.pop()
        backtrack(0,0)
        return res