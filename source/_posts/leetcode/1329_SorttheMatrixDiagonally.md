---
title: 1329. Sort the Matrix Diagonally
tags:  
    - sorting
    - Matrix
categories: leetcode
comments: false
---

## [problem]()
## solution
```c++
class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        // 11 25 66 1 69 7 
        // 23 55 17 45 15 52
        // 75 31 36 44 58 8
        // 22 27 33 25 68 4
        // 84 28 14 11 5 50
        
        // 
        //
        // 14 
        // 22 27
        // 84 28 75
        
        // (2,0)
        // (1,0) (2,1)
        // (0,0) (1,1) (2,2)
        // (0,1) (1,2) (2,3)
        // (0,2) (1,3)
        // (0,3)
        
        
        int n = mat.size(), m = mat[0].size();
        vector<vector<int>> vec(n+m-1);
        int c = 0, i=0;
        vector<int> start = {n-1,0};
        while(c<n+m-1){
            int x = start[0], y = start[1];
            while(x> -1 && x<n && y> -1 && y < m ){
                vec[c].push_back(mat[x++][y++]);
            }
            // sort
            sort(vec[c].begin(), vec[c].end());
            // put order
            x = start[0], y = start[1], i=0;
            while(x> -1 && x<n && y> -1 && y < m && i<vec[c].size()){
                mat[x++][y++] = vec[c][i++];
            }
            c++;
            if(start[0] >0 ) start[0]--;
            else start[1]++;
        }
        return mat;
    }
};
```

## analysis
- time complexity `O(n*n*logn)`
- space complexity `O(nm)` -> `O(n)`