class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        currentValue = 0

        def walk(node):
            nonlocal currentValue
            if not node:
                return False

            currentValue += node.val

            if not node.left and not node.right:
                res = currentValue == targetSum
                currentValue -= node.val
                return res

            if walk(node.left):
                return True
            if walk(node.right):
                return True
            
            currentValue -= node.val
            return False

        return walk(root)