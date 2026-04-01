/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int maxPathSum(TreeNode* root) {
        // algorithm idea we store the max of sum of the nodes below
        // and that node itself. 
        // so basically we start at root and go left and go right. 
        // then keep going down till we hit leaf. once we hit leaf
        // store max sum as leaf value then go up. 
        // then chekc max as stated above.
        int max_sum = INT_MIN;
        maxSum(root, max_sum);
        return max_sum;
    }

    int maxSum(TreeNode* node, int& max_sum) {
        if (node == nullptr) return 0;
        int left = max(0, maxSum(node->left, max_sum));
        int right = max(0, maxSum(node->right, max_sum));

        max_sum = max(max_sum, node->val + left + right);
        return node->val + max(left, right);
    }
};
