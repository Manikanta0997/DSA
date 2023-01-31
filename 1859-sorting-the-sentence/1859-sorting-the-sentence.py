class Solution(object):
    def sortSentence(self, s):
        li = s.split()
        li2 = []
        string = ""
        for i in range(len(li)):
            nu = li[i][len(li[i])-1:len(li[i])]
            li2.append(nu)
            li[i] = li[i][0:len(li[i])-1]
        for i in range(len(li)):
            for j in range(len(li)):
                if(i+1 == int(li2[j])):
                    string = string + " " + li[j]
                    
        string = string[1:len(string)]
        return string
                    
            
        
        