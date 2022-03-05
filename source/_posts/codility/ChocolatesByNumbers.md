---
title: ChocolatesByNumbers
categories: 
    - codility
    - Euclidean algorithm
comments: false
---

## [problem](https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/)



## solution
- `O(N+M)`
```c++
// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;
#include<unordered_set>
int solution(int N, int M) {
    // write your code in C++14 (g++ 6.2.0)
    unordered_set<int> s;
    int n = 0;
    while(s.find(n)==s.end()){
        s.insert(n);
        n = (n+M)%N;

    }
    return s.size();
}
```

#### option 1
```c++
// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int gcd(int n, int m){
    return  m == 0 ? n : gcd(m, n % m);

}
int solution(int N, int M) {
    // write your code in C++14 (g++ 6.2.0)
    // lcm = 20, gcd = 2
    return N/gcd(N,M);
    
}
```