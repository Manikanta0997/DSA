# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        li = []
        def post(root):
            if not root:
                return
            post(root.left)
            li.append(root.val)
            post(root.right)
        post(root)
        return li[k-1]