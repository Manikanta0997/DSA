class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        li = []
        nums = tokens
        top = 0
        z = ["+", "-", '*', '/']
        for i in range(len(nums)):
            val = nums[i]
            if val not in z:
                if top < len(li):
                    li[top] = int(val)
                    top += 1
                else:
                    li.append(int(val))
                    top += 1
            else:
                a = li[top-1]
                b = li[top-2]
                if val == "+":
                    li[top-2] = a + b
                elif val == '-':
                    li[top-2] = b - a
                elif val == '*':
                    li[top-2] = a * b
                elif val =='/':
                    li[top-2] = int(b / a)
                top -= 1
        return li[top - 1]
                    
                    
                
        
        