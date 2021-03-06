---
title: 16. 3Sum Closest
tags:  
    - Two Pointers
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/3sum-closest/submissions/)

## solution
```c++
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int n = nums.size();
        int cand = nums[0] + nums[1] + nums[2];
        for(int i= 0 ;i<n-2;++i){
            int l = i+1, r = n-1;
            while(l<r){
                int sum = nums[i] + nums[l] + nums[r];
                if(sum == target) return target;
                if(sum < target) l++;
                else r--;
                if(abs(cand - target) > abs(sum - target)) cand = sum;
            }
        }
        return cand;
        
    }
};
```
## analysis
- time complexity `O(nlogn)`
- space complexity `O(1)`
