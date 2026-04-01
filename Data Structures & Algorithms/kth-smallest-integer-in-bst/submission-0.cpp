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
    int kthSmallest(TreeNode* root, int k) {
        vector<int> order;
        inorder(root, order);
        return order[k-1];
    }

    void inorder(TreeNode* node, vector<int>& arr) {
        if (node == nullptr) return;
        inorder(node->left, arr);
        arr.push_back(node->val);
        inorder(node->right, arr);
    }
};
