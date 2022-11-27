---
title: 2482. Difference Between Ones and Zeros in Row and Column
tags:
    - dp
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/)
## solution
```c++
class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        vector<int> oneRow(n,0), zeroRow(n,0);
        vector<int> oneCol(m,0), zeroCol(m,0);
        for(int i=0;i<n;++i){
            for(int j = 0;j<m;++j) oneRow[i]+=(grid[i][j] == 1);
            zeroRow[i] = m-oneRow[i];
        }
        for(int j=0;j<m;++j)
        {
            for(int i=0;i<n;++i) oneCol[j] += (grid[i][j] == 1);
            zeroCol[j] = n-oneCol[j];
        }
        vector<vector<int>> diff(n, vector<int>(m, 0));
        for(int i=0;i<n;++i){
            for(int j=0;j<m;++j)
            {
                diff[i][j] = oneRow[i] + oneCol[j] - zeroRow[i] - zeroCol[j]; 
            }
        }
        return diff;      
    }
};
```

## analysis
- time complexity `O(nm)`
- space complexity `O(n)`, `max(O(n), O(m))`