# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        li = []
        def inorder(root):
            if(root != None):
                li.append(root.val)
                inorder(root.left)
                inorder(root.right)
        inorder(root1)
        inorder(root2)
        li.sort()
        return li
        
        