class Solution(object):
    def sortTheStudents(self, score, k):
        li = []
        for i in range(len(score)):
            li.append(score[i][k])
        li2 = []
        for i in range(len(li)):
            li2.append(li[i])
        for i in range(len(li2)):
            for j in range(i,len(li2)):
                if(li2[i] < li2[j]):
                    temp = li2[i]
                    li2[i] = li2[j]
                    li2[j] = temp
        print(li)
        print(li2)
        score1 = []
        for i in range(len(score)):
            score1.append(score[i])
        for i in range(len(score)):
            x = li2[i]
            for k in range(len(score)):
                if(x == li[k]):
                    print(i,k)
                    score[i] = score1[k]
        return score
        
        