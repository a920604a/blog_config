---
categories: leetcode
comments: false
tags:
- MATH
title: '2579. Count Total Number of Colored Cells'
---

## [problem](https://leetcode.com/problems/count-total-number-of-colored-cells/)
## solution

### recursive solution
```c++
class Solution {
public:
    long long coloredCells(int n) {
        // 1: 1
        // 2: 1 + 4 = f(1) + 2*4-4
        // 3: 5 + 8 = f(2) + 3*4-4
        // 4: 13 + 12= f(3) + 4*4-4
        // 5: 25 + 16
        if(n==1) return 1;
        else return coloredCells(n-1) + n*4-4;
    }
};
```

### i solution
```c++
class Solution {
public:
    long long coloredCells(int n) {
        // 1: 1
        // 2: 1 + 4 = f(1) + 2*4-4
        // 3: 5 + 8 = f(2) + 3*4-4
        // 4: 13 + 12= f(3) + 4*4-4
        // 5: 25 + 16
        if(n==1) return 1;
        // else return coloredCells(n-1) + n*4-4;
        long long ret = 1, tmp = 0;
        for(int i=2 ;i<=n; ++i){
            tmp = ret + i*4-4;
            ret = tmp;
        }
        return ret;
    }
};
```

## analysis
- time complexity : could lower to `O(1)` `(long long)n * n + (long long)(n - 1) * (n - 1);`
- space complexity `O(1)`
  