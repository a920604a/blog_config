---
title: 2465. Number of Distinct Averages
tags:
    - sorting
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/count-ways-to-build-good-strings/)

## solution
```c++
class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        
        // low = 3, high = 3, zero = 1, one = 1 
        //dp    1    2  4   8   
        //長度為 i 的建構方法數
        //ret   0   0   0   8
        
        // low = 2, high = 3, zero = 1, one = 2
        // dp   1   1   2   3
        // ret  0   0   2   5  
        int ret = 0, mod = 1000000007;   
        vector<int> dp(high+1, 0);
        dp[0]=1;
        for(int i=1; i<=high;++i)
        {
            if (i >= zero) dp[i] = (dp[i] + dp[i - zero]) % mod;
            if (i >= one) dp[i] = (dp[i] + dp[i - one]) % mod;
            if (i >= low) ret = (ret + dp[i]) % mod;
            
        }
        return ret;     
        
    }
};
```

## analysis
- time complexity `O(n)`
- space complexity `O(n)`