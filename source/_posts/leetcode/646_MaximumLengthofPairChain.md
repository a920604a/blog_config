---
categories: leetcode
comments: false
tags:
- dp
- Greedy
title: 646. Maximum Length of Pair Chain
---

## [problem](https://leetcode.com/problems/maximum-length-of-pair-chain/)
## solution
- dp
```c++
class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        sort( pairs.begin( ), pairs.end( ), [ ]( const vector<int>& lhs, const vector<int>& rhs )
        {
        return lhs[0] < rhs[0]; // also return lhs[1] < rhs[1];
        });
        int ret = 1;
        int n = pairs.size();
        vector<int> dp(n, 1);
        for(int i=1;i<n ;++i)
        {
            vector<int> p = pairs[i];
            for(int j = 0;j<i ;++j)
            {
                vector<int> q = pairs[j];
                if( q[1] < p[0])
                {
                    dp[i] = max(dp[i], 1+dp[j]);
                    ret = max(ret, dp[i]);
                }
            }
        }
        return ret;
        
    }
};
```
- greedy
```c++
class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        sort( pairs.begin( ), pairs.end( ), [ ]( const vector<int>& lhs, const vector<int>& rhs )
        {
        return lhs[1] < rhs[1]; // also return lhs[1] < rhs[1];
        });
        int ret = 0, cur = INT_MIN;
        int n = pairs.size();
        vector<int> dp(n, 1);
         for (const auto& pair : pairs) {
            if (cur < pair[0]) {
                cur = pair[1];
                ret++;
            }
        }
        return ret;
        
    }
};
```
## analysis
- dp solution
    - time complexity `O(n^2)`
    - space complexity `O(n)`
- greedy 
    - time complexity `O(nlogn)`
    - space complexity `O(1)`