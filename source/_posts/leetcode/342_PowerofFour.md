---
title: 342. Power of Four
date: 2022-02-16 16:30:16
tags:  
    - Bit Manipulation
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/power-of-four/)

## solution

```c++
class Solution {
public:
    bool isPowerOfFour(int n) {
        if(n<1) return false;
        if((n&(n-1))!=0) return false;
        return (n&0x55555555) ==n;
    }
};
```

## analysis
- time complexity `O(1)`
- space complexity `O(1)`

