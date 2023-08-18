# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.flag = 0
    def max_depth(self, root):
        if root == None:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right)) 
    def isBalanced(self, root):
        if root == None:
            return True
        self.isBalanced(root.left)
        if root.left != None and root.right != None:
            le = self.max_depth(root.left)
            ri = self.max_depth(root.right)
        elif root.left == None and root.right == None:
            le = 0
            ri = 0
        elif root.left == None:
            le = 0
            ri = self.max_depth(root.right)
        elif root.right == None:
            ri = 0
            le = self.max_depth(root.left)
        if abs(ri - le) > 1:
            self.flag = 1
        self.isBalanced(root.right)
        if self.flag == 1:
            return False
        return True
        
        