import math
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        tot = 0
        x = dict()
        for i in range(len(rectangles)):
            val = rectangles[i][0] / rectangles[i][1]
            if val in x:
                x[val] += 1
            else:
                x[val] = 0
        for i in x:
            if x[i] != 0:
                add = 0
                for i in range(1, x[i]+1):
                    add = add + i
                tot = tot + add
        return tot
            
        
        