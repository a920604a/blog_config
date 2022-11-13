---
title: 2469. Convert the Temperature
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/convert-the-temperature/)

## solution
```cpp
class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        vector<double> ret(2,0);
        ret[0] = celsius+273.15;
        ret[1] = celsius*1.80 + 32.0;
        return ret;
    }
};
```

## analysis
- time complexity `O(1)`
- space complexity `O(1)`