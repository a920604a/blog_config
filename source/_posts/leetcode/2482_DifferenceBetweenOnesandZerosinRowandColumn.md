---
title: 2482. Difference Between Ones and Zeros in Row and Column
tags:
    - matrix
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/)
## solution
```c++
class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        // 0   1   1
        // 1   0   1
        // 0   0   1
        // rows = 2 2   2
        // cols 1   1   3
        int n = grid.size(), m = grid[0].size();
        vector<int> rows(n), cols(m);
        vector<vector<int>> ret(n, vector<int>(m));
        for(int i=0;i<n;++i)
        {
            for(int j=0;j<m;++j){
                 if(grid[i][j]==1) rows[i]++;
            }
        }
        for(int j=0;j<m;++j)
        {
            for(int i=0;i<n;++i) 
                if(grid[i][j]==1) cols[j]++;
        }
        for(int i=0;i<n;++i)
        {
            for(int j=0;j<m;++j)
            {
                ret[i][j] = rows[i] + cols[j] - (m-rows[i]) - (n-cols[j]);
            }
        }
        return ret;
    }
};
```

## analysis
- time complexity `O(nm)`
- space complexity `max(O(n), O(m))`