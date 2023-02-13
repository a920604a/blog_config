---
categories: leetcode
comments: false
tags:
- heap
title: 2558. Take Gifts From the Richest Pile
---

## [problem](https://leetcode.com/problems/take-gifts-from-the-richest-pile/)
## solution

### C++ solution
```c++
class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        priority_queue<int> pq;
        for(int g:gifts) pq.push(g); //  O(nlogn)
        while(k-- ){
            int t = pq.top(); pq.pop();
            pq.push(sqrt(t));
        }
        long long ret = 0 ;
        while(!pq.empty())
        {
            ret += pq.top(); pq.pop();
        }
        return ret;
    }
};
```
### Python solution
```python
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        ret = 0
        nums = [-num for num in gifts]
        heapify(nums)
        while k:
            tmp = math.isqrt(-heappop(nums))
            heappush(nums, -tmp)
            k-=1

        return -sum(nums)
```

## analysis
- time complexity `O(nlogn)` 
- space complexity `O(n)`