# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        def inorder(root):
            if(root != None):
                inorder(root.left)
                inorder(root.right)
                x = root.left
                root.left = root.right
                root.right = x
        inorder(root)
        return root
                
        