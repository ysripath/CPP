/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        // t1 will be the final tree
        if (t1 == NULL && t2 == NULL)
            return NULL;
        if (t2 == NULL)
            return t1;
        if (t1 == NULL)
        {
            t1 = new TreeNode(t2->val);
            t1->left = t2->left;
            t1->right = t2->right;
            return t1;
        }
        t1->val += t2->val;
        t1->left = mergeTrees(t1->left, t2->left);
        t1->right = mergeTrees(t1->right, t2->right);
        return t1;
    }
};
