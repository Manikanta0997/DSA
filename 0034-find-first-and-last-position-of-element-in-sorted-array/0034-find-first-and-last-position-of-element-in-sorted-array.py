class Solution(object):
    def searchRange(self, nums, target):
        start=0
        rear = len(nums)-1
        found = 0
        if(len(nums) > 1):
            for i in range(len(nums)):
                mid = (start + rear) / 2
                if(nums[mid] == target):
                    found = 1
                    break
                elif(nums[mid] > target):
                    rear = mid-1
                elif(nums[mid] < target):
                    start = mid + 1
            if(found == 0):
                return [-1,-1]
            else:
                right = mid
                left = mid
                if(right+1 != len(nums)):
                    while(target == nums[right+1]):
                        right = right+1
                        if(right == len(nums)-1):
                            break
                if(left-1 != -1):
                    while(target == nums[left-1]):
                        left = left - 1
                        if(left <= 0):
                            break
                return [left,right]
        else:
            if(len(nums) == 1):
                if(nums[0] == target):
                    return [0,0]
                else:
                    return [-1,-1]
            else:
                return [-1,-1]
            
        
        