# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxnum = root.val
        def dfs(node, maxnum):
            if not node:
                return 0
            res = 0
            if node.val >= maxnum:
                res += 1
                maxnum = node.val
                
            res += dfs(node.right, maxnum)
            res += dfs(node.left, maxnum)
            return res
        
        return dfs(root, maxnum)
