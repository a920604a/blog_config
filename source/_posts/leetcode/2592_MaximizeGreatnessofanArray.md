---
categories: leetcode
comments: false
tags:
- greedy
title: 2592. Maximize Greatness of an Array
---

## [problem](https://leetcode.com/problems/maximize-greatness-of-an-array/)
## solution

```c++
class Solution {
public:
    int maximizeGreatness(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int l = 0 ,r  = nums.size()-1;
        int  i = n-1;
        while(l<=r) {
            if(nums[i] >= nums[r]) l++; // 打不過就派最小的
            else r--;
            i--;
        }
        return n-r-1;       
    }
};
```


## analysis
- time complexity `O(nlogn)`
- space complexity `O(1)`