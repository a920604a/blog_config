---
title: 113. Path Sum II
tags:  
    - backtracking
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/path-sum-ii/)

## solution
#### option 1 - dfs

```c++
class Solution {
public:
    vector<vector<int>> ret;
    void pathSum(TreeNode* root, int targetSum, vector<int> &path){
        // 終止條件
        if(!root) return;
        targetSum -= root->val;
        path.push_back(root->val);
        // 插入條件
        if(target==0 && !root->left && !root->right) ret.push_back(path);
            // 因為是call by reference 且所以拜訪完葉子後需要pop        
        pathSum(root->left, targetSum, path);
        pathSum(root->right, targetSum, path);
        path.pop_back();
        
    }
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int> path;
        // C++ 同一函數名不同參數是可以的，但同一函數名同參數但不同返回型態是不能的
        pathSum(root, targetSum, path);
        return ret;
    }
};
```