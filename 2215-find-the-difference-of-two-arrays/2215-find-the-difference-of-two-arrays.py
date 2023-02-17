class Solution(object):
    def findDifference(self, nums1, nums2):
        ans1 = []
        ans2 = []
        for i in range(len(nums1)):
            if(nums1[i] not in nums2):
                ans1.append(nums1[i])
        for i in range(len(nums2)):
            if(nums2[i] not in nums1):
                ans2.append(nums2[i])
        ans1 = set(ans1)
        ans2 = set(ans2)
        ans1 = list(ans1)
        ans2 = list(ans2)
        ans1 = [ans1,ans2]
        return ans1
        