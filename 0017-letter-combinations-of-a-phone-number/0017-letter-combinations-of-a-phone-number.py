class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) > 0:
            res = []
            two = 'abc'
            three = 'def'
            four = 'ghi'
            five = 'jkl'
            six = 'mno'
            seven = 'pqrs'
            eight = 'tuv'
            nine = 'wxyz'
            li = [two, three, four, five, six, seven, eight, nine]
            li_index = ['2', '3', '4', '5', '6', '7', '8', '9']
            x = digits[:1]
            for i in range(len(li[li_index.index(x)])):
                res.append(li[li_index.index(x)][i:i+1])

            for i in range(len(digits)-1):
                k = i + 1
                li1 = []
                x = digits[k:k+1]
                for l in range(len(li[li_index.index(x)])):
                    li1.append(li[li_index.index(x)][l:l+1])
                temp = []
                for z in range(len(res)):
                    for g in range(len(li1)):
                        temp.append(res[z] + li1[g])
                res = temp
            return res

        
        