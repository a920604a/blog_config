---
title: 703. Kth Largest Element in a Stream
tags:  
    - heap
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

## solution
```c++
class KthLargest {
private:
    priority_queue<int, vector<int>, greater<int>> pq;
    int size ;
public:
    KthLargest(int k, vector<int>& nums) {
        size = k;
        for(int n:nums){
            pq.push(n);
            if(pq.size() > size) pq.pop();
        }
    }
    int add(int val) {
        pq.push(val);
        if(pq.size() > size) pq.pop();
        return pq.top();
    }
};

```
- 實現BST

