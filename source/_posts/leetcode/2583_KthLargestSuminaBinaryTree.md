---
categories: leetcode
comments: false
tags:
- bfs
title: 2583. Kth Largest Sum in a Binary Tree
---

## [problem](https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/)
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
    long long kthLargestLevelSum(TreeNode* root, int k) {
        vector<long long> levels;
        // level traversal
        queue<TreeNode*> q({root});
        while(!q.empty()) {
            int size = q.size();
            long long level = 0;
            for(int i=0;i<size; ++i) {
                TreeNode *node = q.front();
                q.pop();
                level+=node->val;
                if(node->left != nullptr) q.push(node->left);
                if(node->right != nullptr) q.push(node->right);
                // cout<<node->val<<endl;
            }
            levels.push_back(level);
        }
        
        sort(levels.begin(), levels.end(), greater<long long>());
        if( k-1 >= levels.size()) return -1;
        return levels[(k-1)];
        
    }
};
```
you could replace vector to priority

## analysis
- time complexity `O(nlogn)`
- space complexity `O(n)` 