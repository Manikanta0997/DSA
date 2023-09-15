# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good(root, val):
            if not root:
                return 0
            res = 1 if root.val >= val else 0
            val = max(root.val, val)
            res += good(root.left, val)
            res += good(root.right, val)
            return res
        return good(root, root.val)