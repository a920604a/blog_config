---
categories: leetcode
comments: false
tags: null
title: 2600. K Items With the Maximum Sum
---

## [problem](https://leetcode.com/problems/k-items-with-the-maximum-sum/)
## solution
```c++
class Solution {
public:
    int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        int ret = 0;
        if(numOnes >= k) return k;
        if(numOnes < k) ret = numOnes;
        k-=numOnes;
        if(numZeros >= k) return ret;
        k-=numZeros;
        return ret-k;
        
    }
};
```

## analysis
- time complexity `O(1)`
- space complexity `O(1)`