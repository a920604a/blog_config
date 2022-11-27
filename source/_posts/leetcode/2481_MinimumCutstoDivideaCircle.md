---
title: 2481. Minimum Cuts to Divide a Circle
tags:
    - Math
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/)
## sloution
```c++
class Solution {
public:
    int numberOfCuts(int n) {
        // n, ret
        // (1,0) (2,1) (3,3) (4,2) (5,5) (6,3) (7,7) (8,4) (9,9) (10,5)
        if(n==1) return 0;
        return n%2==0?n/2:n;
        
    }
};
```
## analysis
- time complexity `O(1)`
- space complexity `O(1)`