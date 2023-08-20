---
categories: leetcode
comments: false
tags:
- Prefix Sum
title: 724. Find Pivot Index
---

## [problem](https://leetcode.com/problems/find-pivot-index/)
## solution
```c++
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        // the same with 238. Product of Array Except Self
        
        int n = nums.size();
        vector<int>left(n+2, 0), right(n+2, 0);
        //          1   7   3   6   5   6
        // left  0  1   8   11  17  22  28  -
        //right  -  28  27  20  17  11   6  0
        
        for(int i=1;i<n+1;++i) left[i] = nums[i-1];
        for(int i=1;i<n+1;++i) right[i] = nums[i-1];
        for(int i=2;i<n+1;++i) left[i]+=left[i-1];
        for(int i=n-1;i>0;i--) right[i] +=right[i+1];
        for(int i=1;i<n+1;++i)
        {
            if(left[i-1] == right[i+1]) return i-1;
        }
        return -1;
        
    }
};
```
- reduce space 
```c++
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int right_sum = 0, left_sum= 0;
        for(int n:nums) right_sum +=n;
        int n = nums.size();
        for(int i=0;i<n;++i)
        {
            right_sum-=nums[i];
            if(left_sum == right_sum) return i;
            left_sum+=nums[i];
        }
        return -1;
    }
};
```


## analysis
- time complexity `O(n)`
- space complexity `O(n)` -> `O(1)`
