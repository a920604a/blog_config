---
title: 151. Reverse Words in a String
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/reverse-words-in-a-string/)

## solution

#### option 1 
```c++
class Solution {
public:
    string reverseWords(string s) {
        vector<string> ret;
        string cur;
        int n = s.size();
        for(int i=0;i<n ; ++i){
            char c =s[i];
            if(c == ' '){
                if(!cur.empty()) ret.push_back(cur);
                cur.clear();
                while(i<n && s[i+1] ==' ') i++;
            }
            else cur+=c;
        }
        if(!cur.empty()) ret.push_back(cur);
        reverse(ret.begin(), ret.end());
        string ans;
        for(int i=0;i<ret.size() ; ++i){
            ans+=ret[i];
            if(i!=ret.size()-1) ans+=' ';
        }
        return ans;
        
    }
};
```
#### option 2 
```c++
class Solution {
public:
    string reverseWords(string s) {
        
        int pre = 0, n = s.size();
        for(int i=0;i< n; ++i){
            char c = s[i];
            if(c==' '){
                reverse(s.begin()+pre, s.begin()+i);
                // avoid extra space
                while(i+1<n && s[i+1] ==' ') i++;
                pre = i+1;
            }
        }
        
        reverse(s.begin()+pre, s.end());
        reverse(s.begin(), s.end());
        // trim
        int l=0, r = s.size()-1;
        while(l<r && s[l] == ' ') l++;
        while(l<r && s[r] ==' ') r--;
        s = s.substr(l, r-l+1);
        string ret;
        for(char c:s){
            if(ret.back() ==' ' &&  c==' ') continue;
            ret+=c;
        }
        return ret;
    }
};
```
#### option 3 - stack
```c++
class Solution {
public:
    string reverseWords(string s) {
        stack<string> words;
        int n= s.size();
        int l =0,r =n-1;
        while(l<r && s[l] ==' ') l++;
        while(l<r && s[r] == ' ') r--;

        for(int i=l ; i<r ;)
        {
            if(s[i] == ' ')
            {
                words.push(s.substr(l, i-l));
                cout<<s.substr(l, i-l)<<" ";
                while(i<r && s[i] == ' ') i++;
                l = i;
            }
            else i++;
        }
        words.push(s.substr(l, r-l+1));
        string ret;
        while(!words.empty()){
            string cur = words.top(); words.pop();
            ret+= cur + ' ';
        }
        return ret.substr(0, ret.size() - 1);
    }
};
```
#### option 4 - improved stack

```c++
class Solution {
public:
    string reverseWords(string s) {
        string ret;
        int n= s.size();
        int l =0,r =n-1;
        while(l<r && s[l] ==' ') l++;
        while(l<r && s[r] == ' ') r--;

        for(int i=r ; i>l;)
        {
            if(s[i] == ' ')
            {
                ret+=s.substr(i+1, r+- i )+' ';
                while(i>l && s[i] == ' ') i--;
                r = i;
            }
            else i--;
        }
        ret+=s.substr(l, r-l+1);

        return ret;
    }
};
```
## analysis
- option 1
    - time complexity `O(n)`
    - space complexity `O(n)`
- option 2
    - time complexity `O(n)`
    - space complexity `O(1)`
- 
    - time complexity `O(n)`
    - space complexity `O(n)`
- option 4 
    - time complexity `O(n)`
    - space complexity `O(1)`

