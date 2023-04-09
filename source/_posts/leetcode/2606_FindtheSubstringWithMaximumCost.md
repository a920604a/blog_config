---
categories: leetcode
comments: false
tags:
- dp
- hash table
title: 2606. Find the Substring With Maximum Cost
---

## [problem](https://leetcode.com/problems/find-the-substring-with-maximum-cost/)
## solution
```c++
class Solution {
public:
    unordered_map<char, int> mp;
    int ret = 0;
    void traverse(string s, string path, int cur, int i) {
        if(i> s.size() -1) return;
        if(cur + mp[s[i]]< 0) return;
        ret = max(ret, cur+=mp[s[i]]);
        path+=s[i];
        traverse(s,path, cur, i+1);

    }
    int maximumCostSubstring(string s, string chars, vector<int>& vals) {
        
        char c = 'a';
        for(char i =c; i<='z' ; ++i) mp[i] = 1+ (i-c);
        for(int i=0;i<chars.size() ; ++i) mp[chars[i]] = vals[i];
        
        // traversal
        string path;
        int cur = 0;
        // method 1 => TLE
        // for(int i=0;i<s.size() ; ++i) traverse(s, path,cur, i);
        
        // method 2 dp
        vector<int> dp(s.size(), 0);
        dp[0] = max(mp[s[0]], dp[0]);
        ret = dp[0];
        for(int i=1;i<s.size() ; ++i) {
            if(mp[s[i]] + dp[i-1] > 0) dp[i] = dp[i-1]+ mp[s[i]];
            ret = max(ret, dp[i]);
        }

        return ret;
        
    }
};
```

```c++
class Solution {
public:
    int maximumCostSubstring(string s, string chars, vector<int>& vals) {
        
        vector<int> mp(26,0);
        for(int i=0;i<26 ;++i) mp[i]=i+1;
        for(int i=0;i<chars.size() ; ++i) {
            mp[chars[i]-'a'] = vals[i];
        }
        // Kadane
        int ret = INT_MIN;
        int cur = max(mp[s[0]-'a'], 0);
        ret = max(cur, ret);
        for(int i =1;i<s.size() ; ++i) {
            cur = max(mp[s[i] - 'a'] + cur, 0);
            ret = max(cur, ret);
        }
        return ret;
    }
};
```
## analysis
- time complexity `O(n)`
- space complexity `O(26 + n)` -> `O(1)`