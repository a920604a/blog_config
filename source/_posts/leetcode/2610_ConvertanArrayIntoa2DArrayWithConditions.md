---
categories: leetcode
comments: false
tags: 
-- hash table
title: 2610. Convert an Array Into a 2D Array With Conditions
---

## [problem](https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/)
## solution
```c++
class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        int n = nums.size();
        vector<int> collects(n+1, 0);
        for(int n:nums) collects[n]++;
        vector<vector<int>> rets;
        while(n>0) {
            vector<int> tmp;
            for(int i=1;i<collects.size() ;++i){
                if( collects[i] > 0) {
                    collects[i]--;
                    n--;
                    tmp.push_back(i);
                }
            }
            if(!tmp.empty()) rets.push_back(tmp);
        }
        return rets;
    }
};
```

## analysis
- time complexity `O(mk)` m is length of nums , k is max number range
- space complexity `O(k)`