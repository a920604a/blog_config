---
categories: leetcode
comments: false
title: 2595. Number of Even and Odd Bits
---

## [problem](https://leetcode.com/problems/number-of-even-and-odd-bits/)
## solution

```c++
class Solution {
public:
    vector<int> evenOddBit(int n) {
        vector<int> ret(2,0);
        int idx = 0;
        while(n){
            ret[idx%2]+=n&1; 
            n>>=1;
            idx++;
        }
        return ret;
    }
};
```


## analysis
- time complexity `O(logn)`
- space complexity `O(1)`