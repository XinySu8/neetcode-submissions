# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        length = 1
        if root.right and root.left:
            length += max(self.maxDepth(root.right), self.maxDepth(root.left))
        elif root.right:
            length += self.maxDepth(root.right)
        elif root.left:
            length += self.maxDepth(root.left)
        return length