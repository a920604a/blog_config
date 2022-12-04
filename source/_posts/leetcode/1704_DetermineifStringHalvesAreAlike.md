---
title: 1704. Determine if String Halves Are Alike
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/determine-if-string-halves-are-alike/)

## sloution
```c++
class Solution {
public:
    bool isVowels(char c){
        return (c=='a' || c=='e' || c=='i' || c=='o' || c=='u' || c=='A' || c=='E' || c=='I' || c=='O' || c=='U');
    }
    bool halvesAreAlike(string s) {
        int a =0, b=0 , n=s.size();
        for(int i=0;i<n/2;++i){
            a+=isVowels(s[i]);
            b+=isVowels(s[n-1-i]);
        }
        return a==b;
    }
};
```
## analysis
- time complexity `O(n)`
- space complexity `O(1)`