class Solution(object):
    def addToArrayForm(self, num, k):
        str1 = ''
        for i in range(len(num)):
            str1 = str1 + str(num[i])
        str1 = int(str1)
        k = k + str1
        li = []
        while(k>0):
            li.append(k%10)
            k = k / 10
        for i in range(len(li)/2):
            temp = li[i]
            li[i] = li[len(li)-i-1]
            li[len(li)-i-1] = temp
        
        return li
        
            
            
        