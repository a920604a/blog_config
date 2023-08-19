---
categories: leetcode
comments: false
tags: null
title: 1431. Kids With the Greatest Number of Candies
---

## [problem](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/)
## solution
```c++
class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int n = candies.size();
        int mx = *max_element(candies.begin(), candies.end());
        vector<bool> ret(n, false);
        for(int i =0;i<n;++i)
        {
            ret[i] = candies[i]+extraCandies >= mx? true:false;
        }
        return ret;
    }
};
```


## analysis
- time complexity `O(n)`
- space complexity `O(n)`