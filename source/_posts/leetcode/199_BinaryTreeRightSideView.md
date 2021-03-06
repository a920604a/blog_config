---
title: 199. Binary Tree Right Side View
tags:  
    - backtracking
    - bfs
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/binary-tree-right-side-view/)

## solution
```c++
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ret;
        if(!root) return ret;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int size = q.size();
            for(int i=0;i<size ; ++i){
                TreeNode *p = q.front();
                q.pop();
                if(i==size-1) ret.push_back(p->val);
                if(p->left) q.push(p->left);
                if(p->right) q.push(p->right);
            }
        }
        return ret;
    }
};

```

## analysis
- time complexity `O(n)`
- space complexity `O(n)`