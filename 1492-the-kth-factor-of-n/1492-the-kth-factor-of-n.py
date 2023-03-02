class Solution(object):
    def kthFactor(self, n, k):
        li = []
        for i in range(1,n+1):
            if(n%i==0):
                li.append(i)
        if(k > len(li)):
            return -1
        else:
            return li[k-1]
        