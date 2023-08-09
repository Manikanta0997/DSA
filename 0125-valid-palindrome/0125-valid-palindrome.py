class Solution(object):
    def isPalindrome(self, s):
        str1 = ""
        s = s.lower()
        for i in range(len(s)):
            if (ord(s[i:i+1]) >= 97 and ord(s[i:i+1]) <= 122) or (ord(s[i:i+1]) >= 48 and ord(s[i:i+1]) <= 57):
                str1 = str1 + s[i:i+1]
        n = len(str1)
        for i in range(len(str1) / 2):
            if str1[i:i+1] != str1[n-1-i:n-i]:
                return False
        return True