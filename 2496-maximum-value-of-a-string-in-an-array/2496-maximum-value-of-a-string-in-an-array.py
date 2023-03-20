class Solution(object):
    def maximumValue(self, strs):
        li = []
        for i in range(len(strs)):
            x = strs[i]
            try:
                x = int(x)
                li.append(x)
            except:
                li.append(len(x))
        return max(li)
                