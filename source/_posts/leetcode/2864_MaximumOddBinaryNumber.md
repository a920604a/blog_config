---
categories: leetcode
comments: false
tags: null
title: 2864. Maximum Odd Binary Number
---

## [problem](https://leetcode.com/problems/maximum-odd-binary-number/description)
## solution
```c++
class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int ones=0;
        for(char c:s) ones+=(c=='1');
        string ret(s.size(), '0');
        if(ones==0) return ret;
        else if(ones==1) ret.back() = '1';
        else{
            ret.back() = '1';
            for(int i=0;i<ones-1;i++) ret[i] ='1';
        }
        return ret;
    }
};
```

## analysis
- time complexity 
- space complexity