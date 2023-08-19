---
title: 345. Reverse Vowels of a String
tags:  
    - Two Pointers
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/reverse-vowels-of-a-string/)

## solution
- in-place & swap & two pointers
```c++
class Solution {
public:
    bool isVowel(char &c){
        if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u' || c=='A' || c=='E' || c=='I' || c=='O' || c=='U') return true;
        return false;
    }
    string reverseVowels(string s) {
        int l =0,r = s.size()-1;
        while(l<r){
            while(l<r && !isVowel(s[l])) l++;
            while(l<r && !isVowel(s[r])) r--;
            swap(s[l++],s[r--] );
        }
        return s;
    }
};
```
- stack
```c++
class Solution {
public:
    string reverseVowels(string s) {
        stack<char> vowels;
        for(char c: s)
        {
            if (c == 'a' || c=='e' || c=='i' || c=='o' || c=='u' || c == 'A' || c=='E' || c=='I' || c=='O' || c=='U') vowels.push(c);
        }
        string ret;
        for(char c:s)
        {
            if (c == 'a' || c=='e' || c=='i' || c=='o' || c=='u' || c == 'A' || c=='E' || c=='I' || c=='O' || c=='U'){
                ret += vowels.top();
                vowels.pop();
            }
            else ret+=c;
        }
        return ret;
    }
};
```
## analysis
- time complexity `O(n)`
- space complexity `O(1)`
