---
title: 200. Number of Islands
tags:  
    - backtracking
    - bfs
    - Union Find
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/number-of-islands/)

## solution

#### option 1 - backtracking
將拜訪過的位置，原地修改其陣列的值為 `0`

```c++
class Solution {
public:
    void traverse(vector<vector<char>>& grid, int i, int j){
        int n = grid.size(), m = grid[0].size();
        if(i<0 || j<0 || i>n-1 || j>m-1 || grid[i][j] =='0') return;
        grid[i][j] = '0';
        traverse(grid, i-1, j);
        traverse(grid, i+1, j);
        traverse(grid, i, j-1);
        traverse(grid, i, j+1);
    }
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        int n = grid.size(), m = grid[0].size();
        for(int i=0;i<n;++i){
            for(int j = 0;j<m;++j){
                if(grid[i][j] == '1'){
                    traverse(grid, i, j);
                    count++;
                }
            }
        }
        return count;
        
    }
};
```
#### option 2 - Union Find
## analysis