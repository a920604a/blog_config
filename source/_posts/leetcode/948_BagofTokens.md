---
categories: leetcode
comments: false
tags:
- greedy
- sorting
title: 948. Bag of Tokens
---

## [problem](https://leetcode.com/problems/bag-of-tokens/description/)
## solution

```c++
class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        //  55  71  82, 54
        //  136(-1) -> 81(0) ->10(1)
        sort(tokens.begin(), tokens.end());
        int count = 0,n = tokens.size();
        int l=0, r= n-1;
        while(l<=r && count>=0){
            int k=0;
            int n = power;
            while(n < tokens[l] && count-k>=0){
                n+=tokens[r--];
                k++;
            }
            if(l<=r && count-k>=0) {
                power= n;
                count-=k;
                power-=tokens[l++];
                count++;
            }
        } 
        return count;
    }
};
```
## analysis
- time complexity `O(nlogn)`
- space complexity `O(1)`