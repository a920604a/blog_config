---
title: 2465. Number of Distinct Averages
tags:
    - sorting
categories: leetcode
comments: false
---


## [problem](https://leetcode.com/problems/number-of-distinct-averages/)

## solution
```c++
class Solution {
public:
    int distinctAverages(vector<int>& nums) {
        
        // 0    1   3   4   4   5
        //  2.5 2.5 3.5
        
        sort(nums.begin(), nums.end() );
        unordered_set<float> ret;
        int n = nums.size(),  l = n/2;
        for(int i=0;i<l;++i)
        {
            float t = (nums[i] + nums[n-1-i]);
            ret.insert(t/2);
        }
        return ret.size();
    }
};
```

## analysis
- time complexity `O(nlogn)`
- space complexity `O(n)`