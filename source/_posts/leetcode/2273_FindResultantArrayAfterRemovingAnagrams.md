---
categories: leetcode
comments: false
tags: 
  - hash table
  - sorting
title: 2273. Find Resultant Array After Removing Anagrams

---

## [problem](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/)
## solution
```c++
class Solution {
public:
    vector<string> removeAnagrams(vector<string>& words) {
        vector<string> ret;
        ret.push_back(words[0]);
        int n = words.size();
        string last = words[0];
        sort(last.begin(), last.end());
        for(int i=1;i<n ;++i) {
            string w = words[i];
            sort(w.begin(), w.end());
            if(last == w) continue;
            else {
                ret.push_back(words[i]);
                last = w;
            }
        }
        return ret;
    }
};
```

```c++
class Solution {
public:
    
    vector<string> removeAnagrams(vector<string>& words) {
        int n =words.size();
        stack<int> sta({0});
        vector<string> ret;
        for(int i=1;i<n;++i){
            string temp = words[i];
            sort(temp.begin(), temp.end());
            if(!sta.empty()){
                string a = words[sta.top()];
                sort(a.begin(), a.end());
                if(a==temp) continue;
                else{
                    sta.push(i);
                }
            }
        }
        while(!sta.empty()){
            int i = sta.top();
            ret.push_back(words[i]);
            sta.pop();
        }
        reverse(ret.begin(), ret.end());
        return ret;
        
    }
};
```
## analysis
- time complexity `O(n*mlogm)`
- space complexity `O(n)`