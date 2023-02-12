class Solution(object):
    def kthDistinct(self, arr, k):
        discnt = []
        found = 0
        for i in range(len(arr)):
            if(len(discnt) < k):
                found = 0
                for j in range(len(arr)):
                    if(i != j):
                        if(arr[i] == arr[j]):
                            found = 1
                            break
                if(found == 0):
                    discnt.append(arr[i])
        print(discnt)
        if(len(discnt) != k):
            return ""
        else:
            return discnt[len(discnt)-1]
        
        