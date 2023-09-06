class Solution(object):
    def generate(self, numRows):
        if numRows > 2:
            res = [[1], [1,1]]
            curr = 1
            for i in range(numRows-2):
                x = res[curr]
                p = [1]
                for j in range(len(x)-1):
                    p.append(x[j] + x[j+1])
                p.append(1)
                res.append(p)
                curr += 1
            return res
        if numRows == 1:
            return [[1]]
        else:
            return [[1],[1,1]]
                    
                
                
                
            
        