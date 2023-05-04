# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        li = []
        def preorder(root):
            if(root == None):
                return
            li.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        x = root
        for i in range(len(li)-1):
            root.left = None
            root.right = TreeNode(li[i+1])
            root = root.right
        return x
                