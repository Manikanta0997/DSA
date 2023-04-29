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
        self.i = 0
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
            if(self.i %2 != 0):
                for t in range(len(r)/2):
                    w = r[t]
                    r[t] = r[len(r) - t -1]
                    r[len(r) - t - 1] = w
            self.i = self.i + 1
            self.res.append(r)
            self.rear = self.rear + 1
            if(a != []):
                self.enqueue(a)
        return self.res
class Solution(object):
    def deepestLeavesSum(self, root):
        if(root != None):
            x = queue()
            x.enqueue1(root)
            z = x.dequeue()
            r = z[len(z)-1]
            o = 0
            for i in range(len(r)):
                o = o + r[i]
            return o
                
        
        
        