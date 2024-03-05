---
categories: leetcode
comments: false
tags:
- Two Pointers
title: 1750. Minimum Length of String After Deleting Similar Ends
---

## [problem](https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description)
## solution
```c++
class Solution {
public:
    int minimumLength(string s) {
        int n = s.size();
        int l = 0, r = n-1;
        bool flag = true;
        while( s[l] == s[r] && l!=r ){
            while(l<r && s[l] == s[r] && s[l] ==s[l+1]) l++;
            while(l<r && s[l] == s[r] && s[r] == s[r-1]) r--;
            if(l!=r){
                flag = true;
                l++;
                r--;
            }
            else flag = false;
        }
        if(l==r ) {
            if(flag) return 1;
            else return 0;
        }
        else return r-l+1;
    }
};
```

## analysis
- time complexity `O(1)`
- space complexity `O(1)`