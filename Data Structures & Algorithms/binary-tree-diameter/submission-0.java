/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    private int max_val = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        height(root);    
        return max_val;       
    }

    private int height(TreeNode root) {
        if (root == null) return 0;

        int l = height(root.left);
        int r = height(root.right);

        max_val = Math.max(max_val, l + r);

        return 1 + Math.max(l, r);
    }
}
