---
title: 867. Transpose Matrix
categories: leetcode
comments: false
tags: null
---

## [problem](https://leetcode.com/problems/transpose-matrix/description/)
## solution
```c++
class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        vector<vector<int>> ret(m, vector<int>(n));
        vector<int> cur(n);
        for(int j=0;j<m;++j){
            int k=0;
            for(int i=0;i<n;++i)
            {
                cur[k++] = matrix[i][j];
            }
            // copy cur to ret[j]
            ret[j] = cur;
        }
        return ret;
    }
};
```
```c++
class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        vector<vector<int>> ret(m, vector<int>(n));
        for(int i=0;i<n;++i)
        {
            for(int j=0;j<m;++j)
            {
                ret[j][i] = matrix[i][j];
            }
        }
        return ret;
    }
};
```
## analysis
- time complexity 
- space complexity