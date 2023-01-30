class Solution(object):
    def heightChecker(self, heights):
        he = []
        for i in range(len(heights)):
            he.append(heights[i])
        for i in range(len(he)):
            for j in range(i, len(he)):
                if(he[i] > he[j]):
                    temp = he[i]
                    he[i] = he[j]
                    he[j] = temp
        count = 0
        print(heights)
        for i in range(len(he)):
            if(he[i] != heights[i]):
                count = count + 1
        return count
                
        