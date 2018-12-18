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
    vector<int> allN;
    vector<int> v;
    int convertToNumber()
    {
        bool zFlag = true;
        int n=1;
        
        auto itr = v.begin();
        while (zFlag
              && itr != v.end())
        {
            if (*itr != 0)
            {
                zFlag = false;
                break;
            }
            itr++;
        }
        if (itr == v.end())
            return 0;
        n = *itr;
        itr++;
        while (itr != v.end())
        {
            n = n* 10 + *itr;
            itr++;
        }
        return n;
    }
    void helper(TreeNode* root)
    {
        if (root == NULL)
            return;
        v.push_back(root->val);
        
        // check if leaf node
        if (!root->left && !root->right)
        {
            allN.push_back(convertToNumber());
            v.pop_back();
            return;
        }
        
        helper(root->left);
        helper(root->right);
        v.pop_back();
        return;
        
    }
    int sumNumbers(TreeNode* root) {
        if (root == NULL)
            return 0;
        helper(root);
        int sum = 0;
        for (auto itr : allN)
        {
            sum += itr;
        }
        return sum;
    }
};
