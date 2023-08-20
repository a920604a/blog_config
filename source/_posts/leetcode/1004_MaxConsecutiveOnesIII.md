---
categories: leetcode
comments: false
tags:
- Sliding Window
title: 1004. Max Consecutive Ones III
---

## [problem](https://leetcode.com/problems/max-consecutive-ones-iii/)
## solution

```c++
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        // silding window
        int l =0 , r =0, n=nums.size();
        int p = k;
        int ret= 0, window=0;
        while(r<n)
        {
            int cur = nums[r++];
            if(cur == 0){
                if(p>=0){
                    p--;
                    window++;
                }
            }
            else if(cur==1)
            {
                window++;
            }
            // p == 0 , can continue to rignt move
            while(p < 0)
            {
                int prev = nums[l++];
                if(prev==0)
                {
                    p++;
                    window--;
                }
                else{
                    window--;
                }
            }
            if(p>=0){
                // update
                // cout<<l-1<<" "<<r-1<<" "<<p<<" "<<window<<endl;
                ret = max(ret, window);
            }
        }
        return ret;
    }
};
```
```c++
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        // silding window
        int l =0 , r =0, n=nums.size();
        int p = k;
        int ret= 0, window=0;
        while(r<n)
        {
            int cur = nums[r++];
            if(cur == 0){
                if(p>=0) p--;
            }
            window++;
            // p == 0 , can continue to rignt move
            while(p < 0)
            {
                int prev = nums[l++];
                if(prev==0) p++;
                window--;
            }
            if(p>=0){
                // update
                ret = max(ret, window);
            }
        }
        return ret;
    }
};
```
```c++
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        // silding window
        int l =0 , r =0, n=nums.size();
        int ret=0;
        while(r<n)
        {
            if( nums[r++] == 0){
                if(k>=0) k--;
            }
            // k == 0 , can continue to rignt move
            while(k < 0)
            {
                if(nums[l++]==0) k++;
            }
            if(k>=0){
                // update
                ret = max(ret, r-l);
            }
        }
        return ret;
    }
};
```
## analysis
- time complexity `O(n)`
- space complexity `O(1)`