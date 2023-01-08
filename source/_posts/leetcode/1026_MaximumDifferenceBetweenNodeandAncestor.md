---
title: 1026. Maximum Difference Between Node and Ancestor
tags:  
    - bfs
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor)

## solution
```c++
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
    int ret =0;
    int traverse(TreeNode * root)
    {
        if(!root->left && !root->right) return root->val; 
        // ret = max(abs(root->val - FindMaxChild(root)),abs(root->val - FindMaxChild(root)) )
        // traverse(root->left);
        // traverse(root->right);
        int mn = INT_MAX;
        FindMinChild(root, mn);
        int mx = INT_MIN;
        FindMaxChild(root, mx);
        // cout<<root->val<<endl;
        // cout<<"FindMinChild: "<<mn<<endl;
        // cout<<"FindMaxChild: "<<mx<<endl;
        // cout<<"ret: "<<max(abs(root->val - mn), abs(root->val - mx ) )<<endl;
        ret = max(ret, max(abs(root->val - mn), abs(root->val - mx ) ));
        return max(abs(root->val - mn), abs(root->val - mx ) );
    }

    void FindMinChild(TreeNode * node, int &ret)
    {
        if(!node) return ;
        ret = min(ret, node->val);
        FindMinChild(node->left, ret); 
        FindMinChild(node->right, ret);
    }

    void FindMaxChild(TreeNode * node, int &ret)
    {
        if(!node) return ;
        ret = max(ret, node->val);
        FindMaxChild(node->left, ret); 
        FindMaxChild(node->right, ret);
        
    }
    int maxAncestorDiff(TreeNode* root) {
        
        if(!root) return 0;
        int rmax = traverse(root);
        int leftMax = maxAncestorDiff(root->left);
        int rightMax = maxAncestorDiff(root->right);
        return ret;
        
    }
};
```

## analysis
- the complexity `O(n*n)` can improve to `O(n)`
- space complexity `O(1)`
