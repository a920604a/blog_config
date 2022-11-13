---
title: 2471. Minimum Number of Operations to Sort a Binary Tree by Level
tags:
    - sorting
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/)

## solution
```cpp
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
    
int findMinSwap(vector<int> &arr, int n)
{
    // temporary vector to store values, along with its index in the original vector
    vector<pair<int, int>> temp(n);
    for (int i = 0; i < n; i++)
    {
        // values in the vector
        temp[i].first = arr[i];
        // index of the particular value.
        temp[i].second = i;
    }


    //sort the temp vector according to the values
    sort(temp.begin(), temp.end());
    // variable to store the answer
    int minimum_swaps = 0;
    int i = 0;
    while (i < n)
    {
        // If there is no need to swap then continue
        if (temp[i].second == i or temp[i].first == arr[i])
        {
            ++i;
            continue;
        }
        else
        {
            // swap the values accordingly
            swap(temp[i].first, temp[temp[i].second].first);
            // swap the indices also within the temp array also
            swap(temp[i].second, temp[temp[i].second].second);
            // stay on the same position until, we fulfill the criterion
            if (temp[i].second != i)
                i--;
        }
        //increment the answer
        minimum_swaps++;
        // move to the next index
        ++i;
    }
    return minimum_swaps;
}

    
     vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ret;
        if(!root)return ret;
        queue<TreeNode *>q({root});
        while(!q.empty()){
            int size = q.size();
            vector<int> level;
            for(int i=0;i<size;++i){
                
                TreeNode *p =  q.front();
                q.pop();
                level.push_back(p->val);
                if(p->left) q.push(p->left);
                if(p->right) q.push(p->right);
            }
            ret.push_back(level);
            
        }
        return ret;
    }
    
    int minimumOperations(TreeNode* root) {
        
        vector<vector<int>> level = levelOrder(root);
        int ret = 0;
        for(vector arr:level)
        {
            ret+=findMinSwap(arr, arr.size());
            
        }
        return ret;
        
    }
};
```

## analysis
- time complexity `O(nlogn)`
- space complexity `O(n)`