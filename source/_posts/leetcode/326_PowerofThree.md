---
title: 326. Power of Three

tags:  
    - Bit Manipulation
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/power-of-three/)

## solution

```c++
class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n<1) return false;
        while(n%3==0) n/=3;
        return n==1;
    }
};
```

## analysis
- time complexity `O(1)`
- space complexity `O(1)`

