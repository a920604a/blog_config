---
categories: leetcode
comments: false
tags:
- backtracking
title: 2597. The Number of Beautiful Subsets
---

## [problem](https://leetcode.com/problems/the-number-of-beautiful-subsets/)
## solution

```c++
class Solution {
public:
    vector<vector<int>> subsets;
    void traverse(int l, vector<int>& path, vector<int> &nums, int k) {
        
        if(!path.empty()) subsets.push_back(path);
        
        for(int i=l; i<nums.size(); ++i) {
            if(!path.empty() && !isValid( nums[i], k, path)) continue;
            path.push_back(nums[i]);
            traverse(i+1, path, nums, k);
            path.pop_back();
        }
        
    }
    bool isValid(int target, int k, vector<int> & path) {
        
        for(int i=path.size()-1 ;i>-1;i--) {
            
            if(target - path[i]  ==k){
                return false;
            }
        }
        return true;
    }
    int beautifulSubsets(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        vector<int> path;
        traverse(0, path, nums, k);
        return subsets.size();
        
    }
};
```


## analysis
- time complexity 
- space complexity