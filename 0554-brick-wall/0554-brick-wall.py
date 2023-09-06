class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        li = []
        glo = dict()
        for i in range(len(wall)):
            x = dict()
            tot = 0
            for j in range(len(wall[i])-1):
                x[tot + wall[i][j]] = 1
                tot += wall[i][j]
                if tot not in glo:
                    glo[tot] = 1
            li.append(x)
        count = len(wall)
        for i in glo:
            z = 0
            for j in li:
                if i not in j:
                    z += 1
            count = min(count, z)
        return count
        
            
            
            
            
            
                
                
                        
                        
                    
                
        