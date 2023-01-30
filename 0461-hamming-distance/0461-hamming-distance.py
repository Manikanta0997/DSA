class Solution(object):
    def hammingDistance(self, x, y):
        li1 = []
        li2 = []
        while(x > 0):
            li1.append(x%2)
            x = x / 2
        while(y>0):
            li2.append(y%2)
            y = y/2
        if(len(li1) > len(li2)):
            q = len(li1) - len(li2)
            for i in range(q):
                li2.append(0)
        elif(len(li2) > len(li1)):
            q = len(li2) - len(li1)
            for i in range(q):
                li1.append(0)
        count = 0
        for i in range(len(li1)):
            if(li1[i] != li2[i]):
                count = count + 1
        return count