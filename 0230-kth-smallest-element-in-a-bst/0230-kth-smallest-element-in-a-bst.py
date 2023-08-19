# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.count = 0
        self.ele = 0
    def kthSmallest(self, root, k):
        if root == None:
            return
        self.kthSmallest(root.left, k)
        self.count += 1
        if self.count == k:
            self.ele = root.val
        self.kthSmallest(root.right, k)
        if self.count == 1:
            return root.val
        else:
            return self.ele
            
        
        
        