---
title: 2483. Minimum Penalty for a Shop
tags:
    - Prefix Sum
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/minimum-penalty-for-a-shop/)

## solution
```c++
class Solution {
public:
    int bestClosingTime(string customers) {
        // 從右往左，數(N=0) 個數
        // 從左往右，數(Y=1) 個數
        int n = customers.size();
        vector<int> left(n+1,0), right(n+1,0);
        int total = 0;
        for(char c:customers) total+=(c=='Y');
        left[0] = total;
        right[n] = n-total;
        int p = total;
        for(int i=0;i<n;++i){
            if(customers[i] =='Y') p--;
            left[i+1] = p;
        }
        for(int i=n-1,  p = n-total;i>-1;i--)
        {
            if(customers[i] == 'N') p--;
            right[i] = p;
        }
        
        for(int i=0;i<n+1;++i) left[i] +=right[i];
        
        // find index of  minimum value ;
        int idx= -1, value = 100001;
        for(int i=0;i<n+1;++i)
        {
            if(left[i] < value ){
                 idx = i;value = left[i];
            }
        }
        return idx;
    }
};
```

## analysis
- time complexity `O(n)`
- space complexity `O(n)`