---
title: 2530. Maximal Score After Applying K Operations
tags:
    - heap
categories: leetcode
comments: false
---


## [problem](https://leetcode.com/problems/maximal-score-after-applying-k-operations/)

## solution

```c++
class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        long long ret = 0 ;
        // select max value in vector
        priority_queue <int> pq;
        for(int n:nums) pq.push(n);
        while(k--){            
            double t =pq.top();
            ret+=t;
            pq.pop();
            pq.push(ceil(t/3));
        }
        return ret;
        
    }
};
```

## analysis
- time complexity `O(Klogn)` ,  K is the number of query
- space complexity `O(n)`