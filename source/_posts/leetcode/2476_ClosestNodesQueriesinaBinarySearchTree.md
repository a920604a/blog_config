---
title: 2476. Closest Nodes Queries in a Binary Search Tree
tags:
    - Binary Search
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/)

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
    void traverse(TreeNode *root, vector<int> &ret){
        if(root == nullptr) return;
        traverse(root->left, ret);
        ret.push_back(root->val);
        traverse(root->right, ret);
        
    }
    vector<vector<int>> closestNodes(TreeNode* root, vector<int>& queries) {

        vector<vector<int>> res(queries.size(), vector<int> (2, 0));
        vector<int> nums;
        traverse(root, nums);
        int n = nums.size();
        // for(int r:nums) cout<<r<<" ";
        for(int q=0;q<queries.size() ; ++q){
            if(queries[q]<nums[0]){
                    res[q][0] =-1;
                    res[q][1] = nums[0];
            }
            else if(queries[q] > nums[n-1]){
                    res[q][0] = nums[n-1];
                    res[q][1] = -1;
            }
            else{
                // 1 2 4 6 9 13 14 15 
                // binary search
                int l = 0, r = n-1;
                while(l<=r){
                    int mid = l + (r-l)/2;
                    if(nums[mid] == queries[q]){
                        res[q][0] = nums[mid];
                        res[q][1] = nums[mid];
                        break;
                    }
                    if(nums[mid] > queries[q]) r = mid-1;
                    else l = mid+1;
                }
                if(res[q][0]==0)
                {
                    res[q][0] = min( nums[l],  nums[r]);
                    res[q][1] =  max( nums[l],  nums[r]);
                }
                
                
            }
        }
        return res;
        
    }
};
```

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
    void traverse(TreeNode *root, vector<int> &ret){
        if(root == nullptr) return;
        traverse(root->left, ret);
        ret.push_back(root->val);
        traverse(root->right, ret);
    }
    vector<vector<int>> closestNodes(TreeNode* root, vector<int>& queries) {

        vector<vector<int>> res;
        vector<int> nums;
        traverse(root, nums);
        int n = nums.size();
        
        for(int q: queries){
            auto it = lower_bound(begin(nums), end(nums), q);
            if (it != end(nums) && *it == q)
                res.push_back({q, q});
            else
                res.push_back({it == begin(nums) ? -1 : *prev(it), it == end(nums) ? -1 : *it});
            
                
        }
        return res;
        
    }
};
```

## analysis
- time complexity `O(mlogn)`
- space complexity `O(n)`