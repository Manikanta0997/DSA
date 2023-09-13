class Solution:
    def decodeString(self, s: str) -> str:
        li = []
        res = ''
        for i in range(len(s)):
            if s[i:i+1] != ']':
                li.append(s[i:i+1])
            else:
                res = ''
                while li[-1] != '[':
                    res = li.pop() + res
                li.pop()
                num = ''
                while li and li[-1].isdigit():
                    num = li.pop() + num
                li.append(int(num) * res)
        return ''.join(li)
                    
                
            
                
                
        