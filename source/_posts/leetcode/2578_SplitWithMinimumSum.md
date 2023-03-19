
---
categories: leetcode
comments: false
tags:
- greedy
- sorting
title: 2578. Split With Minimum Sum
---

## [problem](https://leetcode.com/problems/split-with-minimum-sum/)
## solution

### C++ solution
```c++
class Solution {
public:
    int splitNum(int num) {
        int ret = 0;
        vector<int> nums;
        while(num ){
            nums.push_back(num%10);
            num/=10;
        }
        sort(nums.begin(), nums.end());
        if(nums.size()%2!=0) nums.insert(nums.begin(), 0);
        int n = nums.size();
        for(int i=0;i< n;++i) {
            if(i%2==0) ret*=10;
            ret+=nums[i];
        }
        return ret;        
    }
};
```

### python solution
```python
class Solution:
    def splitNum(self, num: int) -> int:
        nums = list()
        ret = 0
        while(num):
            nums.append(num%10)
            num//=10
        nums.sort()
        
        if(len(nums)%2!=0):
            nums = [0] + nums
        
        for i, v in enumerate(nums):
            if(i%2==0):
                ret*=10
            ret+=v
        return ret
```

## analysis
- time complexity `O(nlogn)`
- space complexity `O(n)`