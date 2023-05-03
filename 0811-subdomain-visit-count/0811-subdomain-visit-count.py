class Solution(object):
    def subdomainVisits(self, cpdomains):
        count = []
        domain = []
        for i in range(len(cpdomains)):
            z = cpdomains[i]
            z = z.split(' ')
            count.append(int(z[0]))
            domain.append(z[1])
        z = len(domain)
        for i in range(z):
            x = domain[i]
            y = x.split('.')
            for j in range(len(y)-1):
                p = ''
                for k in range(j+1, len(y)):
                    if(k != len(y) - 1):
                        p = p + y[k] + '.'
                    else:
                        p = p + y[k]
                domain.append(p)
                count.append(count[i])
        res = []
        resc = []
        for i in range(len(count)):
            x = domain[i]
            y = count[i]
            for j in range(i+1,len(count)):
                r = domain[j]
                if(x == r):
                    y = y + count[j]
            if x not in res:
                res.append(x)
                resc.append(y)
        for i in range(len(res)):
            res[i] = str(resc[i]) + " " + res[i]
        return res
                    