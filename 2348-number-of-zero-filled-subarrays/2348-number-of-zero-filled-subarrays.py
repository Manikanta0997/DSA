class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l = 0
        x = dict()
        while l < len(nums):
            if nums[l] == 0:
                app = ''
                while nums[l] == 0 and l < len(nums):
                    app = app + '0'
                    l += 1
                    if l >= len(nums):
                        break
                if app in x:
                    x[app] += 1
                else:
                    x[app] = 1
            else:
                l += 1
        tot = 0
        for i in x:
            z = len(i)
            tot = tot + (int(z * (z + 1) / 2)) * x[i]
        return tot
                
                
        