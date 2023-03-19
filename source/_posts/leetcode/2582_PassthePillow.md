---
categories: leetcode
comments: false
tags:
- math
title: 2582. Pass the Pillow
---

## [problem](https://leetcode.com/problems/pass-the-pillow/d)
## solution
```c++
class Solution {
public:
    int passThePillow(int n, int time) {
        // 1-2-3-4-3-2-1-2-3-4
        // pattern is 1-2-3-4-3-2
        vector<int> lines;
        for(int i=1;i<=n;++i) lines.push_back(i);
        for(int i=n-1;i>1 ;i--) lines.push_back(i);
        return lines[time%(2*n-2)];      
    }
};
```


```c++
class Solution {
public:
    int passThePillow(int n, int time) {
        // 1-2-3-4-3-2-1-2-3-4
        // pattern is 1-2-3-4-3-2
        // vector<int> lines;
        // for(int i=1;i<=n;++i) lines.push_back(i);
        // for(int i=n-1;i>1 ;i--) lines.push_back(i);
        // return lines[time%(2*n-2)];   
        time%=(2*n-2);
        if(time > n-1 ) return n-time%(n-1);
        else return time+1;
    }
};
```

## analysis
- time complexity `O(n)` could lower to `O(1)`
- space complexity `O(n)` could lower to `O(1)`