---
categories: leetcode
comments: false
tags:
- greedy
- sorting
- Prefix sum
title: 2587. Rearrange Array to Maximize Prefix Score
---

## [problem](https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/)
## solution

```c++
class Solution {
public:
    int maxScore(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>());
        int count = (nums.front()>0)?1:0;
        long long cur = nums[0];
        for(int i=0;i<nums.size() ; ++i) {
            if(i==0) continue;
            cur += nums[i];
            if(cur > 0) count++;
            else break;
        }
        return count ; 
    }
};
```


## analysis
- time complexity `O(nlogn)`
- space complexity `O(1)`