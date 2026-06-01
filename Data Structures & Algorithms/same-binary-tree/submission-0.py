# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(nodep, nodeq):
            if not nodep and not nodeq:
                return True
            elif nodep and nodeq and nodep.val != nodeq.val:
                return False
            elif nodep and nodeq and nodep.val == nodeq.val:
                return dfs(nodep.left, nodeq.left) and dfs(nodep.right, nodeq.right)
            elif not nodep or not nodeq:
                return False
            return True
        return dfs(p, q)
            