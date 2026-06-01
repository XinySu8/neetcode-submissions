# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def isSametree(nodep, nodeq):
            if not nodep and not nodeq:
                return True
            if nodep and nodeq and nodep.val == nodeq.val:
                return isSametree(nodep.left, nodeq.left) and isSametree(nodep.right, nodeq.right)
            return False
        
        if isSametree(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

        