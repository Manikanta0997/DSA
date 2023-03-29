# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        def fun(root):
            count = 0
            if(root.val %2 == 0):
                if(root.left != None):
                    if(root.left.left != None):
                        count = count + root.left.left.val
                    if(root.left.right != None):
                        count = count + root.left.right.val
                if(root.right != None):
                    if(root.right.left != None):
                        count = count + root.right.left.val
                    if(root.right.right != None):
                        count = count + root.right.right.val
            return count
        self.val = 0
        def inorder(root):
            if(root !=None):
                self.val = self.val + fun(root)
                inorder(root.left)
                inorder(root.right)
        inorder(root)
        return self.val
            
        