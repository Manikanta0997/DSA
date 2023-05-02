class Solution(object):
    def isCircularSentence(self, sentence):
        li = sentence.split(' ')
        y = 0
        for i in range(len(li)-1):
            z = li[i]
            x = li[i+1]
            if(z[len(z)-1] != x[0]):
                y = 1
                break
        if(li[len(li)-1][len(li[len(li)-1])-1] != li[0][0]):
            y = 1
        if(y == 0):
            return True