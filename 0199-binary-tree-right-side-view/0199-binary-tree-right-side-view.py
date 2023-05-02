# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class queue:
    def __init__(self):
        self.li = []
        self.top = 0
        self.rear = 0
        self.res = []
    def enqueue(self, root):
        self.li.append(root)
        self.top = self.top + 1
    def enqueue1(self, root):
        self.li.append([root])
        self.top = self.top + 1
    def dequeue(self):
        while(self.top > self.rear):
            z = self.li[self.rear]
            r = []
            a = []
            for d in range(len(z)):
                i = z[d]
                r.append(i.val)
                if(i.left != None):
                    a.append(i.left)
                if(i.right != None):
                    a.append(i.right)
            self.res.append(r)
            self.rear = self.rear + 1
            if(a != []):
                self.enqueue(a)
        return self.res
                
class Solution(object):
    def rightSideView(self, root):
        if(root != None):
            x = queue()
            x.enqueue1(root)
            y = x.dequeue()
            res = []
            for i in range(len(y)):
                res.append(y[i][len(y[i])-1])
            return res
        