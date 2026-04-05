class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        
        def get_height(node):
            nonlocal max_diameter
            if not node:
                return 0
            
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            # Update the global maximum diameter found so far
            max_diameter = max(max_diameter, left_height + right_height)
            
            # Return the height of the current node to its parent
            return 1 + max(left_height, right_height)

        get_height(root)
        return max_diameter