#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        stack = []
        for i in range(len(start)):
            stack.append((start[i], end[i], i+1))
        stack.sort(key = lambda x: x[1])
        endtime = stack[0][0]-1
        count = 0
        for i in stack:
            if i[0] > endtime:
                count += 1
                endtime = i[1]
        return count
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends