class Solution(object):
    def xorOperation(self, n, start):
        li = []
        for i in range(n):
            li.append(start + 2*i)
        xor = li[0]
        for i in range(n-1):
            xor = xor ^ li[i+1]
        return xor
        