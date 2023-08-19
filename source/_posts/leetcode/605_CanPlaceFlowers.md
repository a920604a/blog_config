---
categories: leetcode
comments: false
tags: null
title: 605. Can Place Flowers
---

## [problem](https://leetcode.com/problems/can-place-flowers/)
## solution
```c++
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int len = flowerbed.size();
        
        // corner case
        if(len==1){
            if(flowerbed[0] == 1) return n>0?false:true;
            else if(flowerbed[0]==0) return n>1?false:true;
        }
        vector<int> ret = flowerbed;
        int m = n;
        if(flowerbed[1] == 0  &&  flowerbed[0]==0){
            m--;
            ret[0] = 1;
        }
        for(int i = 1;i<len-1 ; ++i)
        {
            if(flowerbed[i-1] == 0 && flowerbed[i] == 0 && flowerbed[i+1]==0 && ret[i-1]==0)
            {
                ret[i] =1;
                m--;
            }
        }
        if(flowerbed[len-2] == 0 && ret[len-2]==0 && flowerbed[len-1] == 0){
            m--;
            ret[len-1] =1;
        }
        return m>0?false:true;
    }
};
```
```c++
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int len = flowerbed.size();
        
        // corner case
        if(len==1){
            if(flowerbed[0] == 1) return n>0?false:true;
            else if(flowerbed[0]==0) return n>1?false:true;
        }
        int m = n;
        if(flowerbed[1] == 0  &&  flowerbed[0]==0){
            m--;
            flowerbed[0] = 1;
        }
        for(int i = 1;i<len-1 ; ++i)
        {
            if(flowerbed[i-1] == 0 && flowerbed[i] == 0 && flowerbed[i+1]==0){
                flowerbed[i] = 1;
                m--;
            }
        }
        if(flowerbed[len-2] == 0 && flowerbed[len-1] == 0) {
            flowerbed[len-1] = 1;
            m--;
        }
        return m>0?false:true;
    }
};
```


## analysis
- time complexity `O(n)`
- space complexity `O(n)` -> `O(1)`