---
categories: leetcode
comments: false
tags:
- hash table
title: 1436. Destination City
---

## [problem](https://leetcode.com/problems/destination-city/)
## solution


```c++
class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_map<string, string> mp;
        string ret;
        for(auto path:paths)
        {
            mp[path[0]] = path[1];
        }
        
        string city = paths[0][0];
        while(mp.find(city)!=mp.end())
        {
            ret = mp[city];
            city = mp[city];
        }
        return ret;
        
    }
};
```

## analysis
- time complexity `O(n)`
- space complexity `O(n)`