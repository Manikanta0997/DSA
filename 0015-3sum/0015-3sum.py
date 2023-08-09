class Solution(object):
    def threeSum(self, nums):
        '''nums.sort()
        li = []
        n = len(nums)
        print(nums)
        for i in range(len(nums)-2):
            l = i + 1
            r = n-1
            x = nums[i]
            while(l < r):
                if x + nums[l] + nums[r] == 0:
                    li.append([x,nums[l],nums[r]])
                    if(nums[l] == nums[l+1] and nums[r] == nums[r-1]):
                        while nums[l] == nums[l+1]:
                            l = l + 1
                    elif nums[l] == nums[l+1]:
                        r = r - 1
                    elif nums[r] == nums[r]:
                         l = l + 1
                elif x + nums[l] + nums[r] > 0:
                    r = r - 1
                elif x + nums[l] + nums[r] < 0:
                    l = l + 1
        print(li)'''
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
