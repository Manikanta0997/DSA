
class Solution(object):
    def kClosest(self, points, k):
        li = []
        res = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            li.append(x ** 2 + y ** 2)
        li, points = zip(*sorted(zip(li, points)))
        x = []
        for i in range(k):
            x.append(points[i])
        return x
            
        