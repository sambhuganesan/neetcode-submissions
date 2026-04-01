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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return subTree(0, preorder.size()-1, 0, preorder, inorder);   
    }   

    TreeNode* subTree(int left, int right, int indx, vector<int>& preorder, vector<int>& inorder) {
        if (left > right) return nullptr;
        int val = preorder[indx];

        int val_indx = 0;
        for (val_indx = 0; val_indx < inorder.size(); val_indx++) {
            if (inorder[val_indx] == val) break;
        }
        TreeNode* node =  new TreeNode(val);

        node->left = subTree(left, val_indx-1, indx+1, preorder, inorder);
        node->right = subTree(val_indx+1, right, indx + (val_indx - left) + 1, preorder, inorder);

        return node;
    }
};
