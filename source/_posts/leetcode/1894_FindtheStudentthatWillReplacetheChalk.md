---
title: 1894. Find the Student that Will Replace the Chalk
tags:  
    - Binary Search
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/)

## solution
- brute force , TLE
```c++
class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        // brute force , TLE
        int i=0, size = chalk.size();
        while(k - chalk[i%size] >= 0){
            k -= chalk[i%size];
            i++;
        }
        return i%size;
    }
};
```

#### option 1 - math to prune 
```c++
class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        // prune , save time
        int total = 0, n= chalk.size();
        for(int i = 0;i<n;++i){
            total += chalk[i];
            if(k-total<0) return i;
        }
        int times = k/total;
        k-= times*total;
        for(int i=0;i<n;++i){
            if(k-chalk[i]<0) return i;
            k-=chalk[i];
        }
        return -1;
    }
};
```

#### option 2 - Binary Search
```c++
class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        // prune , save time
        // prefix
        int n = chalk.size();
        vector<int> prefix(n,0);
        int total = 0;
        for(int i = 0;i<n;++i){
            total += chalk[i];
            prefix[i]  =total;
            if(k-total<0) return i;
        }
        // use Binary Search which location k can insert
        int times = k/total;
        if(k%total == 0) return 0;
        k-= times*total;
        //  3   7   8   10
        int l = 0 , r = n-1;
        while(l<=r){
            int mid = l + (r-l)/2;
            if(prefix[mid] == k) return mid+1;
            if(prefix[mid] < k) l = mid+1;
            else r= mid-1;
        }
        return l;
    }
};
```