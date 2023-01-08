---
title: 2496. Maximum Value of a String in an Array
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/)

## solution
```c++
class Solution {
public:
    int maximumValue(vector<string>& strs) {
        int ret = -1;
        int count = 0;
        for(string str:strs)
        {
            bool leadZeros = true;
            bool alpha = false;
            for(char c:str){
                if(c>=97 && c<= 122 ){
                    alpha = true;
                    break;
                }
                else if(c=='0' && leadZeros) continue;
                else{
                    leadZeros = false;
                    count =  10*count + (c-'0');
                }
                
            }
            if(alpha) ret = max(ret, (int)str.size());
            else ret = max(ret, count);
            count = 0; 
        }
        return ret;
        
    }
};
```
## analysis
- time complexity `O(nm)`
- space complexity `O(1)`