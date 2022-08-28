---
title: 2315. Count Asterisks
categories: leetcode
comments: false
---


## [problem](https://leetcode.com/problems/count-asterisks/)

## solution

```c++
class Solution {
public:
    int countAsterisks(string s) {
        int ret = 0;
        bool flag = false;
        for(int i=0;i<s.size() ;i++){
            if(s[i]=='|'){
                i++;
                while(i<s.size() && s[i]!='|') i++;
                // i++;
            }
            else{
                if(s[i]=='*') ret++;
                // i++;
            }
        }
        return ret;
    }
};
```

## analysis
- time complexity `O(n)`
- space complexity `O(1)`