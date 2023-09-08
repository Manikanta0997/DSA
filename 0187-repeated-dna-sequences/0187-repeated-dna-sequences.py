class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        x = dict()
        for i in range(len(s) - 9):
            z = s[i:i+10]
            if z in x:
                if x[z] == 1:
                    res.append(z)
                x[z] += 1
            else:
                x[z] = 1
        return res
            
        