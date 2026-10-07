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
class Solution
{
public:
    int sumOfLeftLeaves(TreeNode *root)
    {
        this->dfs(root, ' ');
        return this->leaves_count;
    }

private:
    int leaves_count = 0;
    void dfs(TreeNode *root, char dist)
    {
        if (root == nullptr)
        {
            return;
        }

        if (dist == 'L' && root->left == nullptr && root->right == nullptr)
        {
            this->leaves_count += root->val;
            return;
        }

        dfs(root->left, 'L');
        dfs(root->right, 'R');
    }
};