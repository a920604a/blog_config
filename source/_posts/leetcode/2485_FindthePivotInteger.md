---
title: 2485. Find the Pivot Integer
tags:
    - Prefix Sum
    - Binary 
    - Math
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/find-the-pivot-integer/)

## solution
- prefix sum
```c++
class Solution {
public:
    int pivotInteger(int n) {
        if(n == 1) return n;
        int total = (n*(n+1))/2;
        int left = 0;
        for(int i=1;i<=n;++i){
            left +=i;
            if(left == total) return i;
            total-=i;
        }
        return -1;
    }
};
```
- binary search
```c++
class Solution {
public:
    int pivotInteger(int n) {
        if(n == 1) return n;
        int total = (n*(n+1))/2;
        int l= 0, r = n-1;
        while(l<=r){
            int mid = l + (r-l)/2;
            int left = ((mid+1)*mid)/2;
            int right = (n+mid)*(n-mid+1)/2;
            if(left == right) return mid;
            else if(left < right) l = mid+1;
            else r = mid-1;
        }
        return -1;
    }
};
```
- [Math](https://leetcode.com/problems/find-the-pivot-integer/discuss/2851954/O(sqrt(n))-oror-Simple-Maths-proof)
```c++
class Solution {
public:
    int pivotInteger(int n) {
        int ans = (n*n+n)/2;
        int sq = sqrt(ans);
        if(sq * sq == ans)return sq;
        else return -1;
        return -1;
    }
};
```
## analysis
- prefix sum
    - time complexity `O(n)`
    - space complexity `O(1)`
- binary search
    - time complexity `O(logn)`
    - space complexity `O(1)`
- Math
    - time complexity `O(sqrt(n))`
    - space complexity `O(1)`