# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        if(root != None):
            li = []
            def tr(root):
                if root == None:
                    return
                tr(root.left)
                li.append(root.val)
                tr(root.right)
            tr(root)
            return li
        