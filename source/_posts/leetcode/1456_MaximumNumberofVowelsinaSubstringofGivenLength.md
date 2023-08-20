---
categories: leetcode
comments: false
tags:
- Sliding Window
title: 1456. Maximum Number of Vowels in a Substring of Given Length
---

## [problem](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)
## solution
```c++

class Solution {
public:
    bool isVowel(char c)
    {
        return c=='a' || c=='e' || c=='i' || c=='o' || c=='u';
    }
    int maxVowels(string s, int k) {
        int l=0, r= 0, n=s.size();
        unordered_map<char, int> mp;
        int mp_size = 0;
        int ret = 0;
        while(r<n)
        {
            char c = s[r++];
            if(isVowel(c) ){
                mp[c]++;
                mp_size ++;
            }
            if(r-l== k)
            {
                ret = max(ret, mp_size);
                char d = s[l++];
                if(isVowel(d)){
                    mp[d]--;
                    mp_size--;
                }
            }
        }
        return ret;
    }
};
```

## analysis
- time complexity `O(n)`
- space complexity `O(1)`