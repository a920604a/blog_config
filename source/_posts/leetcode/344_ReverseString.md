---
title: 344. Reverse String
tags:  
    - Two Pointers
categories: leetcode
comments: false
---


## [problem](https://leetcode.com/problems/reverse-string/)

## solution
```c++
class Solution {
public:
    void reverseString(vector<char>& s) {
        reverse(s.begin(), s.end());
    }
};
```
#### option 1 - Two Pointers
```c++
class Solution {
public:
    void swap(char *a, char* b){
        *a = *a^*b;
        *b = *a^*b;
        *a = *a^*b;
    }
    void reverseString(vector<char>& s) {
        int l =0, r=s.size()-1;
        while(l<r) swap(&s[l++], &s[r--]);
    }
};

```

#### option 2 - stack
```c++
class Solution {
public:
    void reverseString(vector<char>& s) {
        stack<char> sta;
        for(auto c:s) sta.push(c);
        for(auto &c :s){
            c = sta.top();
            sta.pop();
        }
    }
};

```

#### option 3 - without loop , using recursive
```c++
class Solution {
public:
    void reverseString(vector<char>& s) {
        if(s.size() != 1){
        char temp = s[0];
        s.erase(s.begin());
        reverseString(s);
        s.push_back(temp);
       }
    }
};
```

## analysis
- option 1 - Two Pointers
    - time complexity `O(n)`
    - space complexity `O(1)`
- option 2 - stack
    - time complexity `O(n)`
    - space complexity `O(n)`