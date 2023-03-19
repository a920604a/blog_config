---
categories: leetcode
comments: false
tags:
- heap
title: 2593. Find Score of an Array After Marking All Elements
---

## [problem](https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/)
## solution

```c++
class Solution {
public:
    long long findScore(vector<int>& nums) {
        auto comp = [](vector<int> &a, vector<int> &b){
            if(a[0] == b[0]) return a[1] > b[1];
            return a[0] > b[0];
        };
        priority_queue< vector<int> , vector<vector<int>> , decltype(comp)> pq(comp);
        int n = nums.size();
        // vector<bool> visit(n, false);
        unordered_set<int> visit;
        for(int i=0;i<n;++i) pq.push({nums[i],i} );
        long long score = 0;
        
        while( !pq.empty()) {
            vector<int> cur = pq.top();
            pq.pop();
            if(visit.count(cur[1])) continue;
            
            score += cur[0] ;
            visit.insert(cur[1]);
            if(cur[1]-1 > -1) visit.insert(cur[1]-1);
            if(cur[1] +1 < n) visit.insert(cur[1]+1);
        }
        return score;
    }
};
```


## analysis
- time complexity `O(nlogn)`
- space complexity `O(n)`