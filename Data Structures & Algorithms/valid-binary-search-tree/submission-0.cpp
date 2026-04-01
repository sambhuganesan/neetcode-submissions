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
    bool isValidBST(TreeNode* root) {
        return valid(root, INT_MIN, INT_MAX);
    }

    bool valid(TreeNode* node, int min, int max) {
        if (node == nullptr) return true;
        bool good = true;
        if (node->val <= min || node->val >= max) {
            good = false;
            return good;
        }

        bool left = valid(node->left, min, node->val);
        bool right = valid(node->right, node->val, max);

        good = left && right;
        return good;
        
    }
};
