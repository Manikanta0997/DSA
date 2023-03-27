# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self, sum1 = 0):
        self.sum1 = sum1
    def bstToGst(self, root):
        if(root != None):
            self.bstToGst(root.right)
            root.val = root.val + self.sum1
            self.sum1 = root.val
            self.bstToGst(root.left)
        return root
        
                    
                
        