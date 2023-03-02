class Solution(object):
    def topKFrequent(self, nums, k):
        unique = set(nums)
        unique = list(unique)
        occ = []
        for i in range(len(unique)):
            occ.append(nums.count(unique[i]))
        occ, unique = zip(*sorted(zip(occ, unique)))
        o = []
        for i in range(k):
            o.append(unique[len(occ)-i-1])
        return o
            
        