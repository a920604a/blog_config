---
title: 2470. Number of Subarrays With LCM Equal to K
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/)

## solution
```cpp
class Solution {
public:
    int subarrayLCM(vector<int>& nums, int k) {
        unsigned int n= nums.size(), ret = 0;
        for(int i=0;i<n;++i)
        {
            unsigned int t = nums[i];
            for(int j=i;j<n;j++)
            {
                t= lcm(t, nums[j]);
                if(t==k) ret++;
            }
        }
        
        return ret;
    }
};
```

## analysis
- time complexity `O(n^2)`
- space complexity `O(1)`