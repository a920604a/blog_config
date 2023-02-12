---
categories: leetcode
comments: false
tags:
- binary search
- two pointer
title: 2563. Count the Number of Fair Pairs
---

## [problem](https://leetcode.com/problems/count-the-number-of-fair-pairs/)
## solution
```c++
class Solution {
public:
    int findFirstGreat(vector<int> & nums, int l, int r, int target)
    {
        while(l <= r){
            int mid = l + (r-l)/2;
            int eval = nums[mid];
            if(eval <  target ) l = mid+1;
            else r = mid-1;
        }
        return l;
    }
    int findFirstGreatThan(vector<int> & nums, int l, int r, int target)
    {
        while(l < r){
            int mid = l + (r-l)/2;
            int eval = nums[mid];
            if(eval <=  target ) l = mid+1;
            else r = mid-1;
        }
        return l;
    }
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        long long count = 0;
        // binary search
        sort(nums.begin(), nums.end());
        for(int i=0;i<n-1;++i)
        {
            int s = lower - nums[i], t = upper - nums[i];
            // find the first greater and equal than lower and upper;
            int a = findFirstGreat(nums, i+1, n-1, s);
            int b = findFirstGreatThan(nums, i+1, n -1 , t);

            if( b >= 0 && a >= 0 && b < n && a < n){
                if(nums[a] >= s && nums[b]  <= t) {
                    count += (b-a+1);
                    cout<<(b-a+1)<<endl;
                }
                else if(nums[a] >= s && nums[b-1] <=t){
                    count += b-a;
                    cout<<b-a<<endl;
                }
            }

        }
        return count;
        
        
    }
};

```
## analysis
- time complexity `O(nlogn)`
- space complexity `O(1)`