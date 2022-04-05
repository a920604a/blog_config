---
title: 183. Customers Who Never Order
tags:  
    - Database
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/customers-who-never-order/)
## solution 
sub-query
```sql
# Write your MySQL query statement below

select name as Customers
from Customers as a
where a.id not in(
    select customerId
    from Orders
);
```