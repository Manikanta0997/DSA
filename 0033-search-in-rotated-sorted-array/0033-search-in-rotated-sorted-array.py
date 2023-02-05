class Solution(object):
    def search(self, nums, target):
        t = 1
        index = 0
        if(len(nums)>1):
            for i in range(len(nums)-1):
                if(nums[index] > nums[index+1]):
                    break
                else:
                    index = index + 1
            li1 = nums[0:index+1]
            li2 = nums[index+1:len(nums)]
            start = 0
            end = len(li1)-1
            found1 = -1
            for i in range(len(li1)):
                mid = (start + end) / 2
                if(li1[mid] == target):
                    found1 = mid
                    break
                elif(li1[mid] > target):
                    end = mid-1
                elif(li1[mid] < target):
                    start = mid + 1
            start = 0
            end = len(li2)-1
            found = -1
            for i in range(len(li2)):
                mid = (start + end) / 2
                if(li2[mid] == target):
                    found = mid + index + 1
                    break
                elif(li2[mid] > target):
                    end = mid-1
                elif(li2[mid] < target):
                    start = mid + 1
            if(found1 == -1 and found == -1):
                return -1
            elif(found1==-1 and found != -1):
                return found
            elif(found1!=-1 and found == -1):
                return found1
        else:
            if(nums[0] == target):
                return 0
            else:
                return -1
            
                
            
        
        