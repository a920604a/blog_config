---
categories: leetcode
comments: false
tags:
- Prefix Sum
title: 2559. Count Vowel Strings in Ranges
---

## [problem](https://leetcode.com/problems/count-vowel-strings-in-ranges)
## solution
```c++
class Solution {
public:
    unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
    bool checkStartAndEndVowel(string word){
        if(word == "") return false;
        bool ret = vowels.count(word.front())==1;
        if(!ret) return false;
        return ret && vowels.count(word.back())==1;
    }
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        int n = words.size(), q = queries.size();
        vector<bool> filters(n, false);
        vector<int> prefixSum(n+1, 0);
        // prefix sum
        //      1    0   1   1   1
        // 0    1    1   2   3   4
        vector<int> ret(q, 0);
        for(int i= 0 ;i<n;++i) filters[i] = checkStartAndEndVowel(words[i]);
        int tmp = 0;
        for(int i=0;i<n;++i){
            tmp += (filters[i]);
            prefixSum[i+1] = tmp;
        }
        for(int i=0;i<q ; ++i){
            ret[i] = prefixSum[queries[i][1]+1] - prefixSum[queries[i][0]];
        }
        return ret;
    }
};
```


## analysis
- time complexity `O(n + m)`, m = queries length, n = words length
- space complexity `O(n + m)` 