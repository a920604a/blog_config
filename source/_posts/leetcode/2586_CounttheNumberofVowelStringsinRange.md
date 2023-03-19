---
categories: leetcode
comments: false
title: 2586. Count the Number of Vowel Strings in Range
---

## [problem](https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/)
## solution

```c++
class Solution {
public:
    unordered_set<char> vowels = {'a','e','i', 'o','u'};
    bool isValid(string word) {
        return vowels.count(word.front()) && vowels.count(word.back());
    }
    int vowelStrings(vector<string>& words, int left, int right) {
        int count = 0;
        for(int i=left ; i<=right ; ++i) {
            if(isValid(words[i])) count++;
        }
        return count;
    }
};
```


## analysis
- time complexity `O(n)`
- space complexity `O(1)`