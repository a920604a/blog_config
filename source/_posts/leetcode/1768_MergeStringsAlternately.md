---
title: 1768. Merge Strings Alternately

categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/merge-strings-alternately/)


## solution
```c++
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n = word1.size(), m = word2.size();
        int l=0, r = 0;
        string str ="";
        // merge
        while(l<n && r<m){
            str+=word1[l++];
            str+=word2[r++];
        }
        while(l<n) str+=word1[l++];
        while(r<m) str+=word2[r++];
        return str;
    }
};
```
```c++
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int l = 0, r = 0;
        int n = word1.size(), m = word2.size();
        string ret ;
        for(int i =0;i< n + m ;)
        {
            if(l < n ){
                ret+=word1[l++];
                i++;
            }
            if( r < m )
            {
                ret+=word2[r++];
                i++;
            }
        }
        return ret;
    }
};
```

## analysis
- time complexity `O(n+m)`
- space complexity `O(1)`