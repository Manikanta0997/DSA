# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self, flag=0):
        self.flag = flag
    def isSameTree(self, p, q):
        if((p==None and q!=None) or (p!=None and q==None)):
                print("ijdfgn")
                self.flag = 1
        if(p != None and q != None):
            if(p.val != q.val):
                self.flag = 1
            
            if((p.left != None and q.left == None) or (p.left == None and q.left != None) or (p.right != None and q.right == None) or (p.right == None and q.right != None)):
                self.flag = 1
            self.isSameTree(p.left,q.left)
            self.isSameTree(p.right,q.right)
        
        if(self.flag == 0):
            
                return 'true'
            
        