---
title: 222. Count Complete Tree Nodes
tags:  
    - backtracking
    - Binary Search
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/count-complete-tree-nodes/)

## solution
```c++
class Solution {
public:
    int countNodes(TreeNode* root) {
        if(!root) return 0;
        
        TreeNode *l = root, *r = root;
        int lh =0, rh= 0 ;
        while(l){
            l=l->left;
            lh++;
        }
        while(r){
            r=r->right;
            rh++;
        }
        if(lh == rh) return pow(2,lh)-1;
        return 1+countNodes(root->left)+countNodes(root->right);
        
    }
};
```
## analysis
- time complexity `O(logn)`
- space complexity `O(n)`