---
categories: leetcode
comments: false
tags:
- Sliding Window
title: 643. Maximum Average Subarray I
---

## [problem](https://leetcode.com/problems/maximum-average-subarray-i/)
## solution
```c++
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double ret = -10000;
        int n = nums.size();
        int l= 0, r = 0;
        double window = 0;
        while(r<n)
        {
            window += nums[r++];
            if(r-l == k)
            {
                ret =max(ret, window/k);
                window-=nums[l++];
            }
        }
        return ret;
    }
};
```

## analysis
- time complexity `O(n)`
- space complexity `O(1)`