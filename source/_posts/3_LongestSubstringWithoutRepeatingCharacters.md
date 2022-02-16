---
title: 3. Longest Substring Without Repeating Characters
date: 2022-02-16 16:10:16
tags: 
    - hash table
    - Sliding Window
categories: leetcode
comments: false
---



## [problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## solution
```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> window;
        int l = 0,r = 0, n = s.size(), ret = 0;
        while(r<n){
            char c = s[r++];
            window[c]++;
            while(window[c]>1){
                char d = s[l++];
                window[d]--;
            }
            ret = max(ret, r-l);
        }
        return ret;
    }
};
```
- vector version 
```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> window(128,0);
        int l =0, r=0, ret = 0, n=s.size();
        while(r<n){
            char c = s[r++];
            window[c]++;
            while(window[c]>1){
                char d = s[l++];
                window[d]--;
            }
            ret = max(ret, r-l);
        }
        return ret;
    }
};

```

## analysis
- time complexity `O(n)`
- space complexity `O(n)`