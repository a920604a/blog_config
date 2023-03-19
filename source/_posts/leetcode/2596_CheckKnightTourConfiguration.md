---
categories: leetcode
comments: false
tags:
- bfs
title: 2596. Check Knight Tour Configuration
---

## [problem](https://leetcode.com/problems/check-knight-tour-configuration/)
## solution
```c++
class Solution {
public:
    bool checkValidGrid(vector<vector<int>>& grid) {
        if(grid[0][0] != 0) return false;
        int count = 0, maxCount = grid.size() * grid.size()-1;
        int x = 0, y = 0;
        int i, j;
        
        // (-1, 2), (-2, 1) , (-2,-1),(-1,-2) , (1,-2), (2, -1), (2,1), (1, 2)
        vector<vector<int>> acts = {
            {-1, 2},
            {-2, 1},
            {-2,-1},
            {-1,-2},
            { 1,-2},
            { 2,-1},
            { 2, 1},
            { 1,  2}
        };
        while(count++ < maxCount) {
            bool flag = false;
            for(vector<int> act : acts) {
                i = x + act[0], j = y + act[1];
                if(i>-1 && j > -1 && i<grid.size() && j < grid[0].size() && grid[i][j] ==count){
                    flag = true;
                    x = i, y =j;
                    break;
                }
            }
            if(flag == false) return false;
        }
        return true;
    }
};
```

## analysis
- time complexity `O(n^2)`
- space complexity `O(1)`