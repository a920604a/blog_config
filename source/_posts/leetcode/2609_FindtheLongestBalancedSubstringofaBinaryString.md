---
categories: leetcode
comments: false
tags: null
title: 2609. Find the Longest Balanced Substring of a Binary String
---

## [problem](https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/)
## solution
```c++
class Solution {
public:
    bool isBalanced(string s){
        if(s.size()%2==1) return false;
        int zeros = s.size()/2, ones = s.size()/2;
        int i=0, j=s.size()-1;
        while(i<j) {
            if(s[i] =='0' && s[j] =='1'){
                i++;j--;
                zeros--;
                ones--;
            }
            else return false;
        }
        return ((zeros==0) & (ones==0));
    }
    int findTheLongestBalancedSubstring(string s) {
        int len = 0;
        // find all substring
        for(int i=0;i<s.size()-1 ;++i) {
            // prune
            if(s[i] =='1') continue;
            for(int j = i+1; j<s.size() ; ++j) {
                if(isBalanced(s.substr(i, j-i+1))){
                    len = max(len, j-i+1);
                    i=j;
                }
            }
        }
        return len;
    }
};
```

```c++
class Solution {
public:
    int findTheLongestBalancedSubstring(string s) {
        int n = s.size();
        int count0 = 0, count1 = 0;
        int len = 0;
        for(int i=0;i<n-1;++i) {
            // i-index as cneter
            if(s[i] == '0' & s[i+1] =='1'){         
                int l = i, r = i+1;
                while(l-1 > -1 && r+1 < n && s[l-1]=='0' && s[r+1] == '1') {
                    l--;
                    r++;
                }
                len = max(len, r-l+1);
            }
        }
        return len;
    }
};
```

```c++
class Solution {
public:
    int findTheLongestBalancedSubstring(string s) {
        int len = 0;
        string tmp = "01";
        //  O(N^2 logN)
        while(tmp.size() <= s.size()) {
            if(s.find(tmp)!=string::npos) len = tmp.size();
            tmp = '0' + tmp + '1';
        }
        return len;
    }
};
```
## analysis
- time complexity `O(n^3)` n is max length of substring -> `O(n^2)` -> `O(n^2 logn)`
- space complexity `O(1)`