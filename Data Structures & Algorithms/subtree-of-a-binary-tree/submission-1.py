# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def sameTree(self, f: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if not f and not s:
            return True

        if not f or not s:
            return False

        if f.val != s.val:
            return False

        if f.val == s.val:
            return self.sameTree(f.left, s.left) and self.sameTree(f.right, s.right)