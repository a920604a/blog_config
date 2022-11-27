---
title: 2486. Append Characters to String to Make Subsequence
tags:
    - Two Pointers
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/)

## solution
```c++
class Solution {
public:
    int appendCharacters(string s, string t) {
        int l =0, r = 0, n =s.size(), m= t.size();
        while(l<n && r<m)
        {
            if(s[l] == t[r]){
                l++;r++;
            }
            else l++;
        }
        return m-r;
    }
};
```

## analysis
- time complexity `O(n)`
- space complexity `O(1)`