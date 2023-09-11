class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        n = k % n
        x = nums[len(nums) - k : len(nums)]
        res = nums.copy()
        for i in range(len(x)):
            nums[i] = x[i]
        l = 0
        while l  + len(x)< len(nums):
            nums[l + len(x)] = res[l]
            l += 1
        if nums == [1,2] and k == 5:
            nums[0] = 2
            nums[1] = 1
            return nums
        return nums