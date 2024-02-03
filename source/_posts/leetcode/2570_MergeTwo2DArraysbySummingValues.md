---
categories: leetcode
comments: false
tags:
- sorting
- Two Pointers
- hash table
title: 2570. Merge Two 2D Arrays by Summing Values
---

## [problem](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/)
## solution

```c++
class Solution {
public:
    vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2) {
        int n = nums1.size(), m = nums2.size();
        vector<vector<int>> rets;
        int l=0, r=0;
        while(l<n && r<m) {
            if(nums1[l][0]==nums2[r][0] )
            {
                rets.push_back({nums1[l][0], nums1[l][1]+ nums2[r][1] });
                l++;r++;
            }
            else if(nums1[l][0] <nums2[r][0] )
            {
                rets.push_back(nums1[l++]);
            }
            else rets.push_back(nums2[r++]);   
        }
        while(l<n) rets.push_back(nums1[l++]);   
        while(r<m) rets.push_back(nums2[r++]);   
        return rets;
    }
};
```

## analysis
- time complexity 
- space complexity