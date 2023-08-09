class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1
        while(True):
            x = numbers[l] + numbers[r]
            if x == target:
                return [l+1, r+1]
            elif x > target:
                r = r - 1
            elif x < target: 
                l = l + 1
        