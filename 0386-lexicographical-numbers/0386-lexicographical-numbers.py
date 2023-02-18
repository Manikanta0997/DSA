class Solution(object):
    def lexicalOrder(self, n):
        li = []
        for i in range(n):
            li.append(str(i+1))
        li.sort()
        for i in range(n):
            li[i] = int(li[i])
        return li