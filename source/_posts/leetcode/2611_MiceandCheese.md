---
categories: leetcode
comments: false
tags:
- heap
- greedy
- sorting
title: 2611. Mice and Cheese
---

## [problem](https://leetcode.com/problems/mice-and-cheese/)
## solution
```c++
class Solution {
public:
    int miceAndCheese(vector<int>& reward1, vector<int>& reward2, int k) {
        // HINT 2 
        // Imagine at first that the second mouse eats all the cheese, then we should choose k types of cheese with the maximum sum of - reward2[i] + reward1[i].
        priority_queue<vector<int>, vector<vector<int>> >pq;
        int n =reward1.size();
        int r = 0;
        vector<bool> visited(n, false);
        for(int i= 0 ;i < n; ++i) pq.push({reward1[i] - reward2[i] , i});
        while(k--){
            vector t = pq.top();
            pq.pop();
            visited[t.back()] = true;
            r+= reward1[t.back()];
        }
        for(int i=0;i<n;++i) r+= !visited[i]?reward2[i]:0;
        return r;
    }
};
```
- one pass
```c++
class Solution {
public:
    int miceAndCheese(vector<int>& reward1, vector<int>& reward2, int k) {
        // HINT 2 
        // Imagine at first that the second mouse eats all the cheese, then we should choose k types of cheese with the maximum sum of - reward2[i] + reward1[i].
        priority_queue<vector<int>, vector<vector<int>> >pq;
        int n =reward1.size();
        int r = 0;
        for(int i= 0 ;i < n; ++i) pq.push({reward1[i] - reward2[i] , i});
        for(int i=0;i<n;++i) {
            vector t = pq.top();
            pq.pop();
            if(k>0) r+= reward1[t.back()];
            else r+= reward2[t.back()];
            k--;
        }
        return r;
    }
};
```
- reduce to sorting array
```c++
class Solution {
public:
    int miceAndCheese(vector<int>& reward1, vector<int>& reward2, int k) {
        int n = reward1.size();
        int r = 0;
        for(int i=0;i<n;++i) {
            reward1[i] -= reward2[i];
            r+=reward2[i];
        }
        sort(reward1.begin(), reward1.end());
        for(int i=0;i<k;++i) r+=reward1[n-1-i];
        return r;
    }
};
```
## analysis
- time complexity `O(nlogn)` 
- space complexity `O(n)`