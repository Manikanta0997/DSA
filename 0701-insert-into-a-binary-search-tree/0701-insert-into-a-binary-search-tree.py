# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insert(self, root, val):
        if(root != None):
            if(root.val > val):
                if(root.left == None):
                    root.left = TreeNode(val)
                    return
                else:
                    self.insert(root.left, val)
            else:
                if(root.right == None):
                    root.right = TreeNode(val)
                    return
                else:
                    self.insert(root.right, val)
    def insertIntoBST(self, root, val):
        self.insert(root, val)
        if(root == None):
            root = TreeNode(val)
        return root
        
        