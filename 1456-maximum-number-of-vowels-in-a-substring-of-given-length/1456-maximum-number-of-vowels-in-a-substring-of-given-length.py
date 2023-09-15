class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        x = dict()
        count = 0
        for i in range(k):
            z = s[i:i+1]
            if z in x:
                x[z] += 1
            else:
                x[z] = 1
            if z == 'a' or z == 'e' or z == 'i' or z == 'o' or z == 'u':
                count += 1
        u = count
        l = count
        for i in range(len(s)-k):
            z = s[i:i+1]
            if z == 'a' or z == 'e' or z == 'i' or z == 'o' or z == 'u':
                count -= 1
            x[z] -= 1
            z = s[i+k:i+k+1]
            if z == 'a' or z == 'e' or z == 'i' or z == 'o' or z == 'u':
                count += 1
            if z in x:
                x[z] += 1
            else:
                x[z] = 1
            l = max(count, l)
        return l
            
            
        