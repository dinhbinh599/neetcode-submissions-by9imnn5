/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public TreeNode InvertTree(TreeNode root) {
        void Invert(TreeNode node){
            if (node == null){
                return;
            }
            
            var temp = node.left;
            node.left = node.right;
            node.right = temp;

            Invert(node.left);
            Invert(node.right);
        }

        Invert(root);
        return root;
 
    }
}
