---
title: 2475. Number of Unequal Triplets in Array
tags:
    - sorting
categories: leetcode
comments: false
---


## [problem](https://leetcode.com/problems/number-of-unequal-triplets-in-array/)

## solution
### solution 1 
```c++
class Solution {
public:
    int unequalTriplets(vector<int>& nums) {
        
        // 2 3 4 4 4
        sort(nums.begin(), nums.end());
        int n = nums.size();
        if(n<3) return 1;
        int count =0;
        for(int i=0;i<n-2;i++){
            for(int j=i+1;j<n-1;++j){
                for(int k = j+1;k<n;++k){
                    if(nums[i]!=nums[j] && nums[j]!=nums[k]) count++;
                }
            }
        }
        return count;
        
    }
};
```


## analysis
- sloution 1
    - time complexity `O(n^3)`
    - space complexity `O(1)`
- solution 2
    - time complexity `O()`