---
categories: leetcode
comments: false
tags:
- Prefix Sum
title: 1732. Find the Highest Altitude
---

## [problem](https://leetcode.com/problems/find-the-highest-altitude/)
## solution
```c++
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int mx_height = 0;
        int cur_height = 0;
        for(int g:gain){
            cur_height += g;
            mx_height = max(mx_height, cur_height);
        }
        return mx_height;
    }
};
```

## analysis
- time complexity `O(n)`
- space complexity `O(1)`