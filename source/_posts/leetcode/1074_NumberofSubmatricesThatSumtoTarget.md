---
categories: leetcode
comments: false
tags:
- Prefix Sum
title: 1074. Number of Submatrices That Sum to Target
---

## [problem](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description/)
## solution
```c++
class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        
        int n = matrix.size(), m = matrix[0].size();
        //  0   1   1
        //  1   3   4
        //  1   4   5
        vector<vector<int>> presum = vector<vector<int>>(n+1, vector<int>(m+1,0));
        for(int i=1;i<=n;++i)
        {
            for(int j=1;j<=m;++j)
            {
                presum[i][j] = matrix[i-1][j-1] + presum[i-1][j] + presum[i][j-1]- presum[i-1][j-1];
            }
        }
        int ret = 0;
        for(int i=1;i<=n;++i)
        {
            cout<<endl;
            for(int j = 1;j<=m;++j)
            {
                for(int x = 0;x<i ; ++x)
                {
                    for(int y = 0;y<j ; y++)
                    {
                        int temp = presum[i][j] - presum[x][j] - presum[i][y] + presum[x][y] ;
                        if(temp == target) 
                        {
                            ret++;
                        }
                    }
                }
            }
        }
        return ret;
    }
};

```

## analysis
- time complexity `O(nnmm)`
- space complexity `O(nm)`