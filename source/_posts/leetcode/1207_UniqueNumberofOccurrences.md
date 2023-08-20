---
categories: leetcode
comments: false
tags:
- hash table
title: 1207. Unique Number of Occurrences
---

## [problem](https://leetcode.com/problems/unique-number-of-occurrences/)
## solution
```c++
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> mp;
        unordered_set<int> s;
        for(int a:arr) mp[a]++;
        for(auto it = mp.begin() ; it!=mp.end() ; ++it)
        {
            if(s.count(it->second)) return false;
            s.insert(it->second);
        }
        return true;
        
    }
};
```

## analysis
- time complexity `O(n)`
- space complexity `O(n)`