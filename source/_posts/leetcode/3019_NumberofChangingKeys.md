---
categories: leetcode
comments: false
tags: null
title: 3019. Number of Changing Keys
---

## [problem](https://leetcode.com/problems/number-of-changing-keys/description/)
## solution
```c++
class Solution {
public:
    int countKeyChanges(string s) {
        int count=0;
        int n = s.size();
        for(int i=1;i<n;++i)
        {
            count+=(tolower(s[i-1]) !=tolower(s[i]));
        }
        
        return count;
    }
};
```


## analysis
- time complexity `O(n)`
- space complexity `O(1)`