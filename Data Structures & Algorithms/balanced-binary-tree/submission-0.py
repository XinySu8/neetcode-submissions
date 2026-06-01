# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        right = self.maxDepth(root.right)
        left = self.maxDepth(root.left)
        
        if right - left > 1 or right - left < -1:
            return False
        
        return self.isBalanced(root.right) and self.isBalanced(root.left)

    def maxDepth(self, cur):
        if not cur:
            return 0
        return 1 + max(self.maxDepth(cur.right), self.maxDepth(cur.left))