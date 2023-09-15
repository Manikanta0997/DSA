class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        r = k-1
        z = arr[l:r+1]
        count = 0
        if sum(z)/len(z) >= threshold:
            count += 1
        add = sum(z)
        for i in range(len(arr) - k):
            add -= arr[i]
            add += arr[i+r+1]
            if add / k >= threshold:
                count += 1
        return count
            
            
        