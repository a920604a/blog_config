---
title: 2491. Divide Players Into Teams of Equal Skill
tags:
    - sorting
    - Two Pointers
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/)

## solution
```c++
class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        int total = 0, n=skill.size();
        for(int s:skill) total+=s;
        if(total%(n/2)!=0) return -1;
        int target = total / (n/2);
        sort(skill.begin(), skill.end());
        long long ret =0;
        for(int l=0, r = n-1;r>l ; l++, r--)
        {
            if(skill[l] + skill[r] != target) return -1;
            else ret+=(long long)(skill[l]*skill[r]);
        }
        return ret;
    }
};
```

## analysis
- time complexity `O(nlogn)`
- space complexity `O(1)`