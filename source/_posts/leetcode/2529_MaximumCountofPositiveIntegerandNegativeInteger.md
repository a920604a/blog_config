---
title: 2529. Maximum Count of Positive Integer and Negative Integer
tags:
    - Binary Search
categories: leetcode
comments: false
---


## [problem](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/)


## solution
- naive
```c++
class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int ne_count = 0, pos_count = 0;
        for(int n:nums){
            if(n < 0) ne_count++;
            else if(n > 0) pos_count++;
        }
        return max(ne_count, pos_count);
        
    }
};
```
- binary search
```c++
class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int n = nums.size();
        // find first position large than 0 
        int l = 0, r = n;
        while(l<r){
            int mid = l + (r-l)/2;
            if(nums[mid] <= 0 ) l = mid +1;
            else r = mid;
        }
        l = r-1;
        while(l> -1 && nums[l] ==0) l--;
        
        return max(n-r, l+1);
        
    }
};
```
## analysis
- time complexity `O(n)` -> `O(logn)`
- space complexity `O(1)`
