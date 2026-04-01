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
    int goodNodes(TreeNode* root) {
        return countGoodPaths(root, INT_MIN);
    }

    int countGoodPaths(TreeNode* node, int max_seen) {
        if (node == nullptr) return 0;
        int count = 0;

        if (node->val >= max_seen) {
            count += 1;
        }

        count += countGoodPaths(node->left, max(max_seen, node->val));
        count += countGoodPaths(node->right, max(max_seen, node->val));    

        return count;
    }
};
