---
title: 2460. Apply Operations to an Array
tags:
    - Two Pointers
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/apply-operations-to-an-array/)

## solution
- One pass
```c++
class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        int n = nums.size();
        vector<int> ret(n,0);
        int k = 0;
        for(int i=0;i<n;++i)
        {
            if(nums[i]==0) continue;
            if(i<n-1 && nums[i] == nums[i+1]){
                i++;
                ret[k++] = nums[i]*2;
            }
            else ret[k++] = nums[i];
            
        }
        return ret;
    }
};
```
- Move Zeroes
```c++
class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        int n = nums.size();
        for(int i=0;i<n-1;++i)
        {
            if(nums[i] == nums[i+1]){
                nums[i]*=2;
                nums[i+1] = 0;
                i++;
            }
        }
        int i=0, j=0;
        for(int i=0;i<n;++i)
        {
            if(nums[i])
            {
                swap(nums[j++], nums[i]);
            }
        }
        return nums;
        
    }
};
```

## analysis
- time complexity `O(1)`
- space complexity `O(n)`