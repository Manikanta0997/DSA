class Solution(object):
    def numberOfBeams(self, bank):
        x = []
        for i in range(len(bank)):
            z = bank[i].count('1')
            if(z != 0):
                x.append(z)
        if(len(x) > 1):
            add = 0
            for i in range(len(x)-1):
                c = (x[i]*x[i+1])
                add = add + c
            return add
        else:
            return 0