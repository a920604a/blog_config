---
title: Sorting
categories: 
    - HackerRank
comments: false
---

## Sorting: Bubble Sort

### solution
```python
def countSwaps(a):
    # Write your code here
    count = 0
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                count+=1
                
    print(f"Array is sorted in {count} swaps.\nFirst Element: {a[0]}  \nLast Element: {a[-1]}")

```
### analysis
- time complexity `O(n^2)`
- space complexity `O(1)`


## Mark and Toys

### solution
```python
def maximumToys(prices, k):
    # Write your code here
    prices.sort()
    count =0
    for p in prices:
        if k-p>=0:
            count+=1
            k-=p
        else:
            return count
        
    return count

```
### analysis
- time complexity `O(nlogn)`
- space complexity `O(1)`

## Sorting: Comparator

### solution
```python 
from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return f"name is {self.name}, score is {self.score}\n"            
    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        elif(a.score == b.score):
            if a.name> b.name:
                return 1
            else:
                return -1

```