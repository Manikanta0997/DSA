class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        nums = []
        while r >= l:
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True
            if mid < len(matrix) - 1 and matrix[mid][0] < target and matrix[mid+1][0] > target:
                nums = matrix[mid]
                break
            elif mid == len(matrix)-1:
                nums = matrix[mid]
                break
            elif matrix[mid][0] > target:
                r = mid -1
            elif matrix[mid][0] < target:
                l = mid + 1
                
        l = 0
        if not nums:
            return False
        r = len(nums)-1
        while r >= l:
            mid = int((l + r) / 2)
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        return False
                    
                
        