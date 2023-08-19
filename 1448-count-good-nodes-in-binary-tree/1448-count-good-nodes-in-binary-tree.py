# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def countgood(root, maxval):
            if root == None:
                return 0
            if root.val >= maxval:
                res =  1
            else:
                res =  0
            maxval = max(root.val, maxval)
            res += countgood(root.left, maxval)
            res += countgood(root.right, maxval)
            return res
        return countgood(root, root.val)
        
            
            
            
        