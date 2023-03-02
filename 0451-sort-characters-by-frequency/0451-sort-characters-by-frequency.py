class Solution(object):
    def frequencySort(self, s):
        li = []
        for i in range(len(s)):
            li.append(s[i:i+1])
        li = set(li)
        li = list(li)
        li_index = []
        for i in range(len(li)):
            li_index.append(s.count(li[i]))
        li_index, li = zip(*sorted(zip(li_index, li)))
        s = ''
        for i in range(len(li)):
            s = s + li_index[len(li)-i-1] * li[len(li)-i-1]
        return s
            