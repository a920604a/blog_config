---
categories: leetcode
comments: false
tags:
- sorting
title: 2605. Form Smallest Number From Two Digit Arrays
---

## [problem](https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/)
## solution

```c++
class Solution {
public:
    int minNumber(vector<int>& nums1, vector<int>& nums2) {
        int val = 10*nums1[0] + nums2[0];
        for(int i=0;i<nums1.size() ; ++i) {
            for(int j = 0;j<nums2.size() ; ++j) {
                if(nums1[i] == nums2[j]) val = min(val, nums1[i]);
                else{
                    val = min(val,10*nums1[i] + nums2[j] );
                    val = min(val,10*nums2[j] + nums1[i] );
                }
            }
        }
        return val;
    }
};
```
- sort
```c++
class Solution {
public:
    int minNumber(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        int val = INT_MAX, val2 = INT_MAX, val3 = INT_MAX;
        int n = nums1.size(), m=nums2.size();
        int i =0,j =0;
        while(i< n &&  j<m) {
            if(nums1[i] == nums2[j]) {
                val = nums1[i];
                break;
            }
            else if(nums1[i] < nums2[j]) i++;
            else j++;
        }
        val2 = 10*nums1[0] + nums2[0];
        val3 = 10*nums2[0] + nums1[0];
        return min(val, min(val2, val3));
    }
};
```
## analysis
- time complexity `O(n^2)` -> `O(nlogn)`
- space complexity `O(1)`