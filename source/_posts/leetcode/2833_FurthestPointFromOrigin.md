---
categories: leetcode
comments: false
tags: null
title: 2833. Furthest Point From Origin
---

## [problem](https://leetcode.com/problems/furthest-point-from-origin/)
## solution
```c++
class Solution {
public:
    int furthestDistanceFromOrigin(string moves) {
        int lcount = 0, rcount =0, count = 0 ;
        for(char c:moves)
        {
            if(c=='L' || c=='_') lcount++;
            if(c=='R' || c=='_') rcount++;
            if(c=='_') count++;
        }
        
        if(lcount > rcount) rcount-=count;
        else lcount-=count;
        return abs(lcount - rcount);
    }
};
```

## analysis
- time complexity `O(n)`
- space complexity `O(1)`