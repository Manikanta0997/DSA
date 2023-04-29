# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insert(self, root, data):
        if(root.val>data):
            if(root.left == None):
                root.left = TreeNode(data)
                return
            else:
                self.insert(root.left, data)
        else:
            if(root.right == None):
                root.right = TreeNode(data)
                return
            else:
                self.insert(root.right,data)
    def bstFromPreorder(self, preorder):
        x = preorder[0]
        root = TreeNode(x)
        for i in range(len(preorder)-1):
            y = preorder[i+1]
            self.insert(root, y)
        return root
        
        
        