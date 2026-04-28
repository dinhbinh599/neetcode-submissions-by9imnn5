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
    public bool IsSubtree(TreeNode root, TreeNode subRoot) {
        if (subRoot == null){
            return true;
        }

        if (root == null){
            return false;
        }

        if (IsSametree(root, subRoot)){
            return true;
        }

        return IsSubtree(root.left, subRoot) || IsSubtree(root.right, subRoot);
    }

    public bool IsSametree(TreeNode q, TreeNode p){
        if (q == null && p == null){
            return true;
        }

        if (q == null || p == null){
            return false;
        }

        if (q.val != p.val){
            return false;
        }

        return IsSametree(q.left, p.left) && IsSametree(q.right, p.right);
    }
}
