class Solution(object):
    def kthSmallest(self, matrix, k):
        li = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                li.append(matrix[i][j])
        li.sort()
        return li[k-1]
        