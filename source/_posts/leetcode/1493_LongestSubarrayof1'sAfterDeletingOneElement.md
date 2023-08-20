---
categories: leetcode
comments: false
tags:
- Sliding Window
title: 1493. Longest Subarray of 1's After Deleting One Element
---

## [problem](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)
## solution
```c++
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        // the same with 1004. Max Consecutive Ones III
        int ret= 0;
        int l=0, r=0, n=nums.size();
        int window =0;
        int del=1;
        while(r<n)
        {
            int cur = nums[r++];
            if(cur == 0){
                if(del>=0){
                    del--;
                }
            }
            else window++;
            while( del<0)
            {
                int prev = nums[l++];
                if(prev==0) del++;
                else window--;
            }
            ret = max(ret, window - del); // - del ,  must delete one element.
             
        }
        return ret;
        
    }
};
```

## analysis
- time complexity `O(n)`
- space complexity `O(`)`