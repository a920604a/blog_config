---
title: 2490. Circular Sentence
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/circular-sentence/)
## solution

```c++
class Solution {
public:
    vector<string> split(string sentence, char sep)
    {
        vector<string> ret;
        string temp ;
        for(char c : sentence){
            if(c==' '){
                ret.emplace_back(temp);
                temp = "";
            }
            else temp+=c;
        }
        ret.emplace_back(temp);
        return ret;
    }
    bool isCircularSentence(string sentence) {
        vector<string> sentences = split(sentence, ' ');
        for(string str:sentences) cout<<str<<" ";
        char last = sentences[0].back();
        int n = sentences.size();
        if(n==1) return sentences[0].front() == sentences[0].back();
        for(int i=1;i<n;++i)
        {
            if(sentences[i][0] == last){
                last = sentences[i].back();
            }
            else return false;
            
        }
        return sentences[0].front() == last;
        
    }
};
```
- one pass
```c++
class Solution {
public:
    bool isCircularSentence(string sentence) {
        int n = sentence.size();
        int l=0, r = n-1;
        if(sentence[l]!=sentence[n-1]) return false;
        r = l;
        while(r<n && sentence[r]!=' ') r++;
        while(r<n){
            l = r-1;
            r++;
            if(sentence[l]!=sentence[r]) return false;
            while(r<n && sentence[r]!=' ') r++;
        }
        return true;
        
    }
};
```
## analysis
- time complexity `O(n)`
- space complexity `O(n)` `O(1)`