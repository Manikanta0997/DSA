class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        li1 = num1.split('+')
        li2 = num2.split('+')
        li1[1] = li1[1].replace('i','')
        li2[1] = li2[1].replace('i','')
        li1[0] = int(li1[0])
        li2[0] = int(li2[0])
        li1[1] = int(li1[1])
        li2[1] = int(li2[1])
        real = li1[0] * li2[0] - li1[1] * li2[1]
        imag = li1[0] * li2[1] + li2[0] * li1[1]
        stri = str(real) + "+" + str(imag) + "i"
        return stri