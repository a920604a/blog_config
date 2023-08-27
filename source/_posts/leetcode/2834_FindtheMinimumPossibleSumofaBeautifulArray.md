---
categories: leetcode
comments: false
tags: 
    - hash table
title: 2834. Find the Minimum Possible Sum of a Beautiful Array
---

## [problem](https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/)
## solution
```c++
class Solution {
public:
    long long minimumPossibleSum(int n, int target) {
        int cur = 1;
        long long  ret = 1;
        unordered_set<int> unallowed ;
        unallowed.insert(target - cur);
        for(int i = 1;i<n;++i)
        {
            cur++;
            while(unallowed.count(cur)) cur++;
            ret+=cur;
            unallowed.insert(target - cur);
        }
        return ret;
    }
};
```

## analysis
- time complexity `O(n)`
- space complexity `O(n)`