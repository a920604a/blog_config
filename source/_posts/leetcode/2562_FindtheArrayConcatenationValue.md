---
categories: leetcode
comments: false
tags: null
title: 2562. Find the Array Concatenation Value
---

## [problem](https://leetcode.com/problems/find-the-array-concatenation-value/)
## solution
### C++ solution
```c++
class Solution {
public:
    int digitLen(int n)
    {
        int len = 0;
        while(n>0){
            n/=10;
            len++;
        }
        return len;
    }    
    long long findTheArrayConcVal(vector<int>& nums) {
        long long ret = 0 ;
        int size = nums.size();
        int l = 0, r = size-1;
        while(l<=r)
        {
            if(l==r) ret += nums[l];
            // else ret += nums[l] * pow( 10, trunc(log10(nums[r])) + 1) +  nums[r]  ;
            else ret += nums[l] * pow( 10, digitLen(nums[r])) +  nums[r] ;
            l++;r--;
        }
        return ret;
    }
};
```
### Python solution
```python
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        sums = 0
        while nums:
            if len(nums) > 1 :
                sums += int(str(nums.pop(0)) + str(nums.pop()))
            else:
                sums += nums.pop()
        return sums

```

## analysis
- time complexity `O(n)`
- space complexity `O(1)`