---
title: 2309. Greatest English Letter in Upper and Lower Case
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/)

## solution
```c++
class Solution {
public:
    string greatestLetter(string s) {
        vector<int> lower(26,0), upper(26,0);
        for(char c:s){
            if(c>=65 && c<=90) upper[c-'A']++;
            else lower[c-'a']++;
        }
        for(int i=25;i>-1;--i){
            if(lower[i]>0 && upper[i]>0){
                
                return string(1, 'A'+i);
            }
        }
        return "";
    }
};
```

## analysis
- time complexity `O(n)`
- space complexity `O(1)`
