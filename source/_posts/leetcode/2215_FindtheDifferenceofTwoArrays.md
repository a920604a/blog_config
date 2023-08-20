---
categories: leetcode
comments: false
tags:
- hash table
title: 2215. Find the Difference of Two Arrays
---

## [problem](https://leetcode.com/problems/find-the-difference-of-two-arrays/)
## solution

```c++
class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<int>> ret(2, vector<int>(0));
        unordered_set<int> num1, num2;
        for(int n:nums1) num1.insert(n);
        for(int n:nums2) num2.insert(n);
        for(auto it=num1.begin() ; it!=num1.end() ; ++it)
        {
            if(!num2.count(*it)) ret[0].push_back(*it);
        }
        
        for(auto it=num2.begin() ; it!=num2.end() ; ++it)
        {
            if(!num1.count(*it)) ret[1].push_back(*it);
        }
        return ret;
    }
};
```
## analysis
- time complexity `O(n)`
- space complexity `O(n)`